import requests
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
        self.verify = (not insecure)
        self.headers = {
            "Authorization": "Token token=\"{}{}\"".format(self.api_key, self.secret_key)
        }
        if 'http' in self.url:
            # URL needs to be a hostname, so remove 'https://'
            self.url = re.sub('https?:\/\/', '', url)
        else:
            self.url = "https://{}".format(self.url)
        # self.browser = httplib.HTTPSConnection(url)
        # if insecure:
        #     context = ssl._create_unverified_context()
        #     self.browser = httplib.HTTPSConnection(url, context=context)

    def _get(self, endpoint, paginate=False):
        if paginate:
            result = []
            page = 1
            per_page = 50
            while True:
                new = requests.get(
                    "{}{}".format(self.url, endpoint),
                    headers=self.headers,
                    verify=self.verify,
                    params={"page": page, "per_page": per_page}).json()
                result += new
                page += 1
                if len(new) < per_page:
                    break
        return requests.get("{}{}".format(self.url, endpoint), headers=self.headers, verify=self.verify).json()

    def environments(self):
        """
        Return a list of environments
        """
        response = self._get("/api/v2/environments.json", paginate=True)
        return [Environment(client=self, json=obj) for obj in response]

    def node_groups(self):
        """
        Return a list of Node Groups
        """
        response = self._get("/api/v2/node_groups.json", paginate=True)
        return [NodeGroup(client=self, json=obj) for obj in response]

    def os_families(self):
        """
        Return a list of OS Families
        """
        response = self._get("/api/v2/operating_system_families.json")
        return [OSFamily(client=self, json=obj) for obj in response]

    def os_types(self):
        """
        Return a list of OS Types
        """
        response = self._get("/api/v2/operating_systems.json")
        return [OSType(client=self, json=obj) for obj in response]

    def jobs(self):
        """
        Return a list of jobs
        """
        response = self._get("/api/v2/jobs.json", paginate=True)
        return [Job(client=self, json=obj) for obj in response]

    def job(self, id):
        """
        Return a single job by ID
        """
        response = self._get("/api/v2/jobs/{}.json".format(id))
        return Job(client=self, json=response)
