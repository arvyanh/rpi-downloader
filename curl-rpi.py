import sys
import requests as req

HEADERS_POST = {'Content-type': 'application/json', 'Accept': 'text/plain'}


SERVERADDR = "http://127.0.0.1:10000"

token=""
for i in range(1, len(sys.argv)):
    token+="\"" + sys.argv[i] + "\""
    token+=" "

print("requesting curl" + token)

# send curl request to server
ret = req.post(SERVERADDR+"/curl", json={"args":token}, headers=HEADERS_POST)

# wait for server returns
if ret.json()['return']=="0":
    print("success")


