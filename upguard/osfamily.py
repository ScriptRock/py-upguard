class OSFamily(object):
    def __init__(self, client=None, json=None):
        self.client = client
        if json:
            self.from_json(json)

    def __repr__(self):
        return "OS Family {} (ID: {})".format(self.name, self.id)

    def from_json(self, json):
        self.id = json["id"]
        self.name = json["name"]
