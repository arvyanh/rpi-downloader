#!/usr/bin/env python

import sys
import requests as req

HEADERS_POST = {'Content-type': 'application/json', 'Accept': 'text/plain'}


SERVERADDR = "http://192.168.1.150:10000"

if len(sys.argv) == 1:
    print("please specify the command")
    print("curl rmall ls")
    sys.exit()

command=sys.argv[1]
token=""

for i in range(2, len(sys.argv)):
    if " " in sys.argv[i]:
        token+="\"" + sys.argv[i] + "\""
    else:
        token+= sys.argv[i] 
    token+=" "


if command=="curl":
    print("requesting curl " + token)
    # send curl request to server
    ret = req.post(SERVERADDR+"/curl", json={"args":token}, headers=HEADERS_POST)

    # wait for server returns
    if ret.json()['return']==0:
        print("success")
    else:
        print(ret.json()['return'])


if command=="youtube-dl":
    print("requesting curl " + token)
    # send curl request to server
    ret = req.post(SERVERADDR+"/youtube-dl", json={"args":token}, headers=HEADERS_POST)

    # wait for server returns
    if ret.json()['return']==0:
        print("success")
    else:
        print(ret.json()['return'])



if command=="wget":
    print("requesting wget " + token)
    # send curl request to server
    ret = req.post(SERVERADDR+"/wget", json={"args":token}, headers=HEADERS_POST)

    # wait for server returns
    if ret.json()['return']==0:
        print("success")
    else:
        print(ret.json()['return'])


elif command=="rmall":
    req.post(SERVERADDR+"/curl/rmall", headers=HEADERS_POST)


elif command=="ls":
    ret = req.get(SERVERADDR+"/curl/ls")
    print(ret.json()['return'])

elif command=="cmd":
    cmd = sys.argv[2]
    token=""
    for i in range(3, len(sys.argv)):
        token+=sys.argv[i]
        token+=" "
    ret = req.get(SERVERADDR+"/cmd", params={"args":token, "cmd":cmd})
    print(ret.json()['return'])

