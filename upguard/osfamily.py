from upguard import UpGuardObject
from upguard.ostype import OSType

class OSFamily(UpGuardObject):
    def __repr__(self):
        return "OS Family {} (ID: {})".format(self.name, self.id)

    def os_types(self):
        status, data = self.client._call(method="GET", endpoint="/api/v2/operating_systems.json")
        return [OSType(client=self, json=obj) for obj in data if obj["operating_system_family_id"] == self.id]
