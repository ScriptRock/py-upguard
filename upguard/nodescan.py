from upguard import UpGuardObject

class NodeScan(UpGuardObject):
    def __repr__(self):
        return "Node Scan {} (ID: {})".format(self.name, self.id)
