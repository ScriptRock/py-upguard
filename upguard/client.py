import httplib
import re
import ssl
import json
from upguard.environment import Environment
from upguard.nodegroup import NodeGroup
from upguard.osfamily import OSFamily
from upguard.ostype import OSType
from upguard.job import Job, JobSource

class Client(object):
    def __init__(self, url, api_key, secret_key, insecure=False):
        self.url = url
        self.api_key = api_key
        self.secret_key = secret_key
        if 'http' in self.url:
            # URL needs to be a hostname, so remove 'https://'
            self.url = re.sub('https?:\/\/', '', url)
        else:
            self.url = "https://{}".format(self.url)
        self.browser = httplib.HTTPConnection(url)
        if insecure:
            context = ssl._create_unverified_context()
            self.browser = httplib.HTTPSConnection(url, context=context)

    def _call(self, method, endpoint, body='', page=1, per_page=100):
        try:
            self.browser.request(
                method,
                "{}{}".format(self.url, endpoint),
                body,
                {"Authorization": "Token token=\"{}{}\"".format(self.api_key, self.secret_key),
                "Content-Type": "application/json",
                "Accept": "application/json"})
            response = self.browser.getresponse()
            data = response.read()

            if response.status == 301:
                raise httplib.HTTPException(
                    "Returned {}, try running with `--insecure` argument".format(response.status))
            elif response.status >= 400:
                raise httplib.HTTPException(
                    "{} {}\n{}".format(
                        str(response.status),
                        response.reason,
                        (data.strip() if data else 'No Data Returned')))
        except httplib.HTTPException as h:
            print h.message
        if response.status >= 300:
            raise httplib.HTTPException("Received a non-200 status: {}".format(response.status))
        return response.status, json.loads(data)

    def environments(self):
        """
        Return a list of environments
        """
        status, data = self._call(method="GET", endpoint="/api/v2/environments.json")
        return [Environment(client=self, json=obj) for obj in data]

    def node_groups(self):
        """
        Return a list of Node Groups
        """
        status, data = self._call(method="GET", endpoint="/api/v2/node_groups.json")
        return [NodeGroup(client=self, json=obj) for obj in data]

    def os_families(self):
        """
        Return a list of OS Families
        """
        status, data = self._call(method="GET", endpoint="/api/v2/operating_system_families.json")
        return [OSFamily(client=self, json=obj) for obj in data]

    def os_types(self):
        """
        Return a list of OS Types
        """
        status, data = self._call(method="GET", endpoint="/api/v2/operating_systems.json")
        return [OSType(client=self, json=obj) for obj in data]

    def jobs(self):
        """
        Return a list of jobs
        """
        status, data = self._call(method="GET", endpoint="/api/v2/jobs.json")
        return [Job(client=self, json=obj) for obj in data]

    def job(self, id):
        """
        Return a single job by ID
        """
        status, data = self._call(method="GET", endpoint="/api/v2/jobs/{}.json".format(id))
        return Job(client=self, json=data)
