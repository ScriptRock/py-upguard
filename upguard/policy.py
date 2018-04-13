from upguard import UpGuardObject

class Policy(UpGuardObject):
    def __repr__(self):
        return "Policy {} (ID: {})".format(self.name, self.id)
