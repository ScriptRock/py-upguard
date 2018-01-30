from upguard import UpGuardObject
from upguard.node import Node

class ConnectionManagerGroup(UpGuardObject):
    def __init__(self, client=None, json=None, **kwargs):
        super(ConnectionManagerGroup, self).__init__(client=client, json=json, **kwargs)
        if self.connection_managers:
            self.connection_managers = [ConnectionManager(client=self.client, json=cm) for cm in self.connection_managers]

    def __repr__(self):
        return "Connection Manager Group {} (ID: {})".format(self.name, self.id)

    def nodes(self):
        nodes = self.client.nodes(details=True)
        return [node for node in nodes if node.connection_manager_group_id == self.id]

class ConnectionManager(UpGuardObject):
    def __repr__(self):
        return "Connection Manager {} (ID: {})".format(self.hostname, self.id)
