from upguard import UpGuardObject

class Organization(UpGuardObject):
    def __repr__(self):
        return "Organization {} (ID: {})".format(self.name, self.id)
