from upguard.node import Node

class Environment(object):
    def __init__(self, client=None, json=None):
        self.client = client
        if json:
            self.from_json(json)

    def __repr__(self):
        return "Environment {} (ID: {})".format(self.name, self.id)

    def from_json(self, json):
        self.id = json["id"]
        self.name = json["name"]
        self.short_description = json["short_description"]
        self.node_rules = json["node_rules"]
        self.url = json["url"]

    def nodes(self):
        status, data = self.client._call(method="GET", endpoint="/api/v2/environments/{}/nodes.json".format(self.id))
        return [Node(client=self.client, id=obj["id"]) for obj in data]
