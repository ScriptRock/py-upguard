from upguard import UpGuardObject

class Diff(UpGuardObject):
    def __repr__(self):
        return "Diff ({} items)".format(self.diff_items_count)
