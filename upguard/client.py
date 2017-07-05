import httplib
import re
import ssl
import json
from upguard.environment import Environment

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
