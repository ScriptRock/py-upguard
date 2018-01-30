from upguard import UpGuardObject

class Event(UpGuardObject):
    types = []

    def __init__(self, client=None, json=None, **kwargs):
        super(Event, self).__init__(client=client, json=json, **kwargs)
        if not Event.types:
            Event.types = self.client._get("/api/v2/events/types.json")
        for eventType in Event.types:
            if eventType["id"] == self.type_id: self.type_name = eventType["name"]

    def __repr__(self):
        return "Event {} ({})".format(self.id, self.type_name)

    def from_json(self, json):
        super(Event, self).from_json(json)
