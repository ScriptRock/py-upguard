from upguard import UpGuardObject

class OSType(UpGuardObject):
    def __repr__(self):
        return "OS Type {} (ID: {})".format(self.name, self.id)
