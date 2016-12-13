import logging
from httplib import HTTPConnection

requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
HTTPConnection.debuglevel = 1
