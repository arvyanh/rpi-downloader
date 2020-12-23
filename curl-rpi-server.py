import os
import sys
import json as js

from threading import Thread 
import threading as th

from flask import Flask, request
import subprocess

CURLDIR = "~/.curlDown/"

def initialize():
    print("initialising ....... ")


app = Flask(__name__)


def shellThread(array):
    out=subprocess.run(array)


def sysThread(string):
    os.system(string)


@app.route("/youtube-dl", methods=["POST"])
def youtube_dl():
    '''
    post request format: {args=" "}

    downloads to curldir
    '''
    request_json=request.get_json()
    args = request_json.get("args")

    print("get youtube-dl request: youtube-dl " + args)
    #returncode=os.system("cd " + CURLDIR + "&&" + "curl " + curlarg + "-O;")

    thread=Thread(target = sysThread, args = ("cd " + CURLDIR + "&&" + "youtube-dl " + args + ";",))
    thread.start()      #unjoined thread?
    return js.dumps({"return":0})


@app.route("/curl/ls", methods=["GET"])
def curl_ls():
    out=subprocess.run(['ls', '/home/pi/.curlDown'], stdout=subprocess.PIPE)
    print("ls returns")
    print(out.stdout.decode("utf-8") )
    return js.dumps({"return":out.stdout.decode("utf-8") })

@app.route("/cmd", methods=["GET"])
def cmd():
    command = request.args.get("cmd")
    args = request.args.get("args")
    print(command)
    out=subprocess.run([command, args], capture_output=True)
    print("run command: " + command, args)
    print(out.stdout.decode("utf-8") )
    print(out.stdout.decode("utf-8") )
    return js.dumps({"return":out.stdout.decode("utf-8") })

@app.route("/curl/rm", methods=["POST"])
def curl_rm():
    filename = request.get_json.get("name")
    out=subprocess.run(['rm', '-r', filename], stdout=subprocess.PIPE)
    return js.dumps({"code":out.returncode})

@app.route("/curl/rmall", methods=["POST"])
def curl_rmall():
    out=subprocess.run(['rm', '-r', "/home/pi/.curlDown"], stdout=subprocess.PIPE)
    out=subprocess.run(['mkdir',  "/home/pi/.curlDown"], stdout=subprocess.PIPE)
    return js.dumps({"code":out.returncode})


@app.route("/curl", methods=["post"])
def curl():
    '''
    post request format: {args=" "}

    downloads to curldir
    '''
    request_json=request.get_json()
    curlarg = request_json.get("args")

    print("get curl request: curl " + curlarg)
    #returncode=os.system("cd " + CURLDIR + "&&" + "curl " + curlarg + "-O;")

    thread=Thread(target = sysThread, args = ("cd " + CURLDIR + "&&" + "curl " + curlarg + ";",))
    thread.start()      #unjoined thread?
    return js.dumps({"return":0})

@app.route("/curl-tofile", methods=["post"])
def curl_noname():
    '''
    post request format: {args=" "}

    downloads to curldir
    '''
    request_json=request.get_json()
    curlarg = request_json.get("args")
    print("get curl request: curl " + curlarg)
    #returncode=os.system("cd " + CURLDIR + "&&" + "curl " + curlarg + "-O;")

    thread=Thread(target = sysThread, args = ("cd " + CURLDIR + "&&" + "curl -O" + curlarg + " ;",))
    thread.start()      #unjoined thread?
    return js.dumps({"return":0})

@app.route("/wget-tofile", methods=["post"])
def wget_tofile():
    '''
    post request format: {args=" "}

    downloads to curldir
    '''
    request_json=request.get_json()
    arg = request_json.get("args")
    print("get curl request: wget" + arg)

    #returncode=os.system("wget -P " + CURLDIR + arg);

    thread=Thread(target = sysThread, args = ("wget -P " + CURLDIR + arg,))
    thread.start()      #unjoined thread?
    return js.dumps({"return":0})

@app.route("/wget", methods=["post"])
def wget():
    '''
    post request format: {args=" "}

    downloads to curldir
    '''
    request_json=request.get_json()
    arg = request_json.get("args")
    print("get curl request: wget" + arg)

    thread=Thread(target = sysThread, args = ("wget " + arg,))
    thread.start()      #unjoined thread?
    #returncode=os.system("wget " + arg);

    return js.dumps({"return":0})

if __name__ == "__main__":
    PORT=sys.argv[1]

    print("starting server on port: " + PORT)


    initialize()
    if sys.argv[2] == "debug":
        app.run(port=PORT)
    else:
        app.run(host='0.0.0.0', port=PORT)
