from upguard import UpGuardObject

class JobStatus:
    Failure = -1
    Pending = 0
    Processing = 1
    Success = 2
    Cancelled = 3

    @staticmethod
    def find(id):
        return {
            -1: 'Failure',
            0: 'Pending',
            1: 'Processing',
            2: 'Success',
            3: 'Cancelled'
        }.get(id, None) # Return None if id was not found

class JobSource:
    TEST_STEP = 1
    TEST_SCRIPT = 2
    POLICY = 3
    NODE = 4
    ENVIRONMENT = 5
    POLICY_VERSION = 6
    NODE_GROUP = 7
    NODE_SCAN = 11
    ENVIRONMENT_NODE_SCAN = 12
    NODE_GROUP_NODE_SCAN = 13
    CONNECTIVITY = 14
    NODE_VULN_SCAN = 15
    NODE_GROUP_VULN_SCAN = 16
    FIND_NODES = 17
    CHANGE_REQUEST_SYNC = 18
    INCIDENT_SYNC = 19
    UNAUTH_CHANGE_CHECK = 20
    ENVIRONMENT_VULN_SCAN = 21
    AD_HOC_NODE_SCAN = 22

    @staticmethod
    def find(id):
        return {
            1: 'TEST_STEP',
            2: 'TEST_SCRIPT',
            3: 'POLICY',
            4: 'NODE',
            5: 'ENVIRONMENT',
            6: 'POLICY_VERSION',
            7: 'NODE_GROUP',
            11: 'NODE_SCAN',
            12: 'ENVIRONMENT_NODE_SCAN',
            13: 'NODE_GROUP_NODE_SCAN',
            14: 'CONNECTIVITY',
            15: 'NODE_VULN_SCAN',
            16: 'NODE_GROUP_VULN_SCAN',
            17: 'FIND_NODES',
            18: 'CHANGE_REQUEST_SYNC',
            19: 'INCIDENT_SYNC',
            20: 'UNAUTH_CHANGE_CHECK',
            21: 'ENVIRONMENT_VULN_SCAN',
            22: 'AD_HOC_NODE_SCAN',
        }.get(id, None) # Return None if id was not found

class Job(UpGuardObject):
    def __repr__(self):
        return "Job {} ({})".format(self.id, JobStatus.find(self.status))

    def from_json(self, json):
        super(Job, self).from_json(json)
