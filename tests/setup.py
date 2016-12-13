import logging
from httplib import HTTPConnection

requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
HTTPConnection.debuglevel = 1

event = { 	"session": { 		"sessionId": "SessionId.52c308ca-c32e-4a72-a225-5b7e26dc1f54", 		"application": { 			"applicationId": "amzn1.ask.skill.fc4b254d-050e-4354-a85d-dd63f2bcd021" 		}, 		"attributes": {}, 		"user": { 			"userId": "amzn1.ask.account.AGBC7S7XDLPHTM5PK6IAFTBNESTUWBGSEP3LB5JUO44ZCY5FEVVPOO4TL6NCKN2Z7VSPIKNYESECUHP6EBHO5DIFAIYI2G5AODVA2OFYOMVQYF3752FC6OMFMA7GID3EN7Z7GBVTGFEF2JHRHIKU672YBTJP6QOW5QUSBSY6XUQ7KV64I3Q5NBJH7PXNOFE4D2KYRKS34G5Q23A", 			"accessToken" : "AAEkNjc0ODdhZmMtMjJjMC00ODU2LThlY2ItODEzNDVjNjdlYTE0vg2n5FVzCBEqmfj34T7tojg4rqHBWY0EiHM-CPgUyj74hHfc3IZeufaju6yBuqzbXP-FF_kyji65XKQVy9QNdg79zCmRH7WLkfGFGaI4fkQ7B8d2JW_5Q_FWPW70bfomCed4rszozaSifwByEUG9qg" 		}, 		"new":  True 	}, 	"request": { 		"type": "IntentRequest", 		"requestId": "EdwRequestId.69545eb1-5d44-4ddc-9026-9972364abadc", 		"locale": "en-US", 		"timestamp": "2016-12-13T13:19:36Z", 		"intent": { 			"name": "AccountSummary", 			"slots": {} 		} 	}, 	"version": "1.0" }
