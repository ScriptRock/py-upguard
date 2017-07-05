from upguard.node import Node

class NodeGroup(object):
    def __init__(self, client=None, json=None):
        self.client = client
        if json:
            self.from_json(json)

    def __repr__(self):
        return "Node Group '{}' (ID: {})".format(self.name, self.id)

    def from_json(self, json):
        self.id = json["id"]
        self.organisation_id = json["organisation_id"] if "organisation_id" in json else None
        self.name = json["name"]
        self.description = json["description"]
        self.node_rules = json["node_rules"]
        self.url = json["url"]

    def nodes(self):
        status, data = self.client._call(method="GET", endpoint="/api/v2/node_groups/{}/nodes.json".format(self.id))
        return [Node(client=self.client, id=obj["id"]) for obj in data]
