#!/usr/bin/env python3

import sys
import json
import struct
import webbrowser

try:
    # Python 3.x version
    # Read a message from stdin and decode it.
    def getMessage():
        rawLength = sys.stdin.buffer.read(4)
        if len(rawLength) == 0:
            sys.exit(0)
        messageLength = struct.unpack('@I', rawLength)[0]
        message = sys.stdin.buffer.read(messageLength).decode('utf-8')
        return json.loads(message)

    while True:
        receivedMessage = getMessage()
        if receivedMessage:
            webbrowser.get("google-chrome").open(receivedMessage)
except AttributeError:
    # Python 2.x version (if sys.stdin.buffer is not defined)
    # Read a message from stdin and decode it.
    def getMessage():
        rawLength = sys.stdin.read(4)
        if len(rawLength) == 0:
            sys.exit(0)
        messageLength = struct.unpack('@I', rawLength)[0]
        message = sys.stdin.read(messageLength)
        return json.loads(message)

    while True:
        receivedMessage = getMessage()
        if receivedMessage:
            webbrowser.get("google-chrome").open(receivedMessage)
except:
    print("Somethibg went wrong!")