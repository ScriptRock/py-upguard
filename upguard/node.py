from upguard import UpGuardObject

class Node(UpGuardObject):
    def __repr__(self):
        return "Node {} (ID: {})".format(self.name, self.id)

    def find(self, id):
        response = self.client._get("/api/v2/nodes/{}.json".format(id))
        return Node(client=self.client, json=response.json())
