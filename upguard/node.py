from upguard import UpGuardObject

class Node(UpGuardObject):
    def __repr__(self):
        return "Node {} (ID: {})".format(self.name, self.id)

    def find(self, id):
        status, data = self.client._call(method="GET", endpoint="/api/v2/nodes/{}.json".format(id))
        return Node(client=self.client, json=data)
