from twisted.protocols.basic import LineReceiver
from twisted.internet import protocol, reactor,base
from PyQt5 import QtCore
import json
import time
import os

# {"A":"b"}
class EchoServer(protocol.Protocol):

    def dataReceived(self, data):
        data_json = json.loads(data.decode())
        print(data)

class EchoFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return EchoServer()

if __name__ == "__main__":
    reactor.listenTCP(6353, EchoFactory())
    print("Server started on port 6353")
    reactor.run()
