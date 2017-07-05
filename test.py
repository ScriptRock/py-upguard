#!/usr/bin/env python

from upguard import Client

print "Environments:"
client = Client(
    url="appliance.upguard.org",
    api_key="0d3e7c470d2ecd8fa17a881cd41130f10b049436e5c19d085576c283b30b1512",
    secret_key="dfbc62ee10884c89b8705685378c766150b80b36448e820fd623312e780c10c1",
    insecure=True)
print client.environments()

print "Default Environment Nodes:"
print client.environments()[0].nodes()
