from upguard import UpGuardObject
from upguard.node import Node

class Environment(UpGuardObject):
    def __repr__(self):
        return "Environment {} (ID: {})".format(self.name, self.id)

    def nodes(self):
        status, data = self.client._call(method="GET", endpoint="/api/v2/environments/{}/nodes.json".format(self.id))
        return [Node(client=self.client).find(id=obj["id"]) for obj in data]
