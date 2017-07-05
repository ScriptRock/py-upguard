class Node(object):
    def __init__(self, client=None, json=None, id=None):
        self.client = client
        if json:
            self.from_json(json)
        if id:
            self.id = id
            status, data = self.client._call(method="GET", endpoint="/api/v2/nodes/{}.json".format(self.id))
            self.from_json(data)

    def __repr__(self):
        return "Node {} (ID: {})".format(self.name, self.id)

    def from_json(self, json):
        self.alternate_password = json["alternate_password"]
        self.connect_mode = json["connect_mode"]
        self.connection_manager_group_id = json["connection_manager_group_id"]
        self.created_at = json["created_at"]
        self.created_by = json["created_by"]
        self.description = json["description"]
        self.environment_id = json["environment_id"]
        self.external_id = json["external_id"]
        self.id = json["id"]
        self.ip_address = json["ip_address"]
        self.last_scan_id = json["last_scan_id"]
        self.last_scan_status = json["last_scan_status"]
        self.mac_address = json["mac_address"]
        self.medium_connection_fail_count = json["medium_connection_fail_count"]
        self.medium_group = json["medium_group"]
        self.medium_hostname = json["medium_hostname"]
        self.medium_password = json["medium_password"]
        self.medium_port = json["medium_port"]
        self.medium_ssl_cert = json["medium_ssl_cert"]
        self.medium_ssl_privkey = json["medium_ssl_privkey"]
        self.medium_type = json["medium_type"]
        self.medium_username = json["medium_username"]
        self.name = json["name"]
        self.node_type = json["node_type"]
        self.online = json["online"]
        self.operating_system_family_id = json["operating_system_family_id"]
        self.operating_system_id = json["operating_system_id"]
        self.organisation_id = json["organisation_id"]
        self.primary_node_group_id = json["primary_node_group_id"]
        self.scan_options = json["scan_options"]
        self.short_description = json["short_description"]
        self.status = json["status"]
        self.updated_at = json["updated_at"]
        self.updated_by = json["updated_by"]
        self.url = json["url"]
        self.uuid = json["uuid"]
        # Info
        if json["info"]:
            self.agent_version = json["info"]["agent_version"]
            self.architecture = json["info"]["architecture"]
            self.hostname = json["info"]["hostname"]
            self.ipaddress = json["info"]["ipaddress"] if "ipaddress" in json["info"] else ""
            self.os_release_version = json["info"]["os_release_version"]
            self.osfamily = json["info"]["osfamily"]
            self.timezone = json["info"]["timezone"]
