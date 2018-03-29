import requests
import re
import ssl
import json
import datetime
from upguard.organization import Organization
from upguard.connectionmanager import ConnectionManagerGroup, ConnectionManager
from upguard.environment import Environment
from upguard.event import Event
from upguard.node import Node
from upguard.nodegroup import NodeGroup
from upguard.osfamily import OSFamily
from upguard.ostype import OSType
from upguard.job import Job, JobSource

class Client(object):
    def __init__(self, url, api_key, secret_key, insecure=False):
        self.session = requests.Session()
        self.session.headers.update({"Authorization": "Token token=\"{}{}\"".format(api_key, secret_key)})
        if insecure:
            requests.packages.urllib3.disable_warnings()
        self.verify = (not insecure)
        self.url = url
        if 'http' in self.url:
            # URL needs to be a hostname, so remove 'https://'
            self.url = re.sub('https?:\/\/', '', url)
        else:
            self.url = "https://{}".format(self.url)

    def _get(self, endpoint, paginate=False, params={}):
        params = params or {}
        if paginate:
            result = []
            if "page" not in params: params["page"] = 1
            if "per_page" not in params: params["per_page"] = 50
            while True:
                new = self.session.get(
                    "{}{}".format(self.url, endpoint),
                    params=params,
                    verify=self.verify).json()
                result += new
                params["page"] += 1
                if len(new) < params["per_page"]:
                    break
            return result
        return self.session.get(
            "{}{}".format(self.url, endpoint),
            params=params,
            verify=self.verify).json()

    def organizations(self, user):
        """
        Return a list of organizations for the given user
        """
        params={}
        if isinstance(user, int):
            params["user_id"] = user
        response = self._get("/api/v2/accounts.json", paginate=False, params=params)
        return [Organization(client=self, json=obj) for obj in response]

    def organisations(self, user):
        """
        Alias for organizations
        """
        self.organizations(user)

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

    def nodes(self, details=False):
        """
        Return a list of Nodes
        """
        response = self._get("/api/v2/nodes.json", paginate=True)
        nodes = [Node(client=self, json=obj) for obj in response]
        if details:
            detailed_nodes = []
            for node in nodes:
                detailed_nodes.append(Node(client=self, json=self._get("/api/v2/nodes/{}.json".format(node.id))))
            return detailed_nodes
        return nodes

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

    def events(self, view_name=None, query=None, since=None, before=None):
        """
        Return a list of events.

        Optionally provide a datetime object `since` to only return events from a certain time
        """
        params={}
        if view_name: params["view_name"] = view_name
        if query: params["query"] = query
        if since: params["start"] = since.strftime("%Y-%m-%d")
        if before: params["end"] = before.strftime("%Y-%m-%d")
        response = self._get("/api/v2/events.json", paginate=True, params=params)
        return [Event(client=self, json=obj) for obj in response]

    def connection_manager_groups(self):
        """
        Return a list of connection manager groups.
        """
        response = self._get("/api/v2/connection_manager_groups.json", paginate=False)
        return [ConnectionManagerGroup(client=self, json=obj) for obj in response]
