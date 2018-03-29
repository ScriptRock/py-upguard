class UpGuardObject(object):
    def __init__(self, client=None, json=None, **kwargs):
        self.client = client
        if json:
            self.from_json(json)
        if kwargs:
            for key, value in kwargs.iteritems():
                setattr(self, key, value)

    def from_json(self, json):
        for property, value in json.iteritems():
            setattr(self, property, value)

from upguard.client import *
from upguard.connectionmanager import *
from upguard.environment import *
from upguard.event import *
from upguard.node import *
from upguard.nodegroup import *
from upguard.osfamily import *
from upguard.ostype import *
from upguard.organization import *
from upguard.job import *
