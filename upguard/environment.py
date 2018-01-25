from upguard import UpGuardObject
from upguard.node import Node

class Environment(UpGuardObject):
    def __repr__(self):
        return "Environment {} (ID: {})".format(self.name, self.id)

    def nodes(self):
        response = self.client._get("/api/v2/environments/{}/nodes.json".format(self.id), paginate=True)
        return [Node(client=self.client).find(id=obj["id"]) for obj in response]
