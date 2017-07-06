from upguard.ostype import OSType

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

    def os_types(self):
        status, data = self.client._call(method="GET", endpoint="/api/v2/operating_systems.json")
        return [OSType(client=self, json=obj) for obj in data if obj["operating_system_family_id"] == self.id]
