from twisted.protocols.basic import LineReceiver
from twisted.internet import protocol, reactor
from PyQt5 import QtCore
import json
import time
import os

clients = {}  # 存储所有客户端连接
livehost = []
# androidServer.py
class EchoServer(LineReceiver):

    def __init__(self,pyqtSignal_str):
        self.pyqtSignal_str = pyqtSignal_str
        self.androidIP = "0.0.0.0"
        self.androidUUID = "000000000"
        self.workListener = "workListener"
        self.totalBytesRead = 0

    def emit_signal(self):
        self.pyqtSignal_str.emit(self.client_address)

    def connectionMade(self):
        self.client_address = self.transport.getPeer().host
        print(f"New connection from {self.androidIP}")
        clients.update({self.client_address:self})
        self.emit_signal()

    def send_response(self, response_data):
        self.transport.write(json.dumps(response_data).encode())
        self.transport.write(b"\n")

    def parse_data(self, data):
        return json.loads(data.decode())

    def dataReceived(self, data):
        data_json = self.parse_data(data)
        if data_json.get("fileReceiverReady") == "ok":
            print("服务器就绪")
            self.send_response({self.workListener: "fileFileNameReady"})
            print("提示服务器准备接收文件名")

        elif data_json.get("fileFileNameReady") == "ok":
            print("服务器已准备接收文件名")
            self.send_response({self.workListener: "filename","actualFileName":self.filename,"totalBytesRead":self.totalBytesRead})
            print(f"文件名 [{self.filename}] 已发送")

        elif data_json.get("filename") == "ok":
            print("发送文件数据")
            with open(self.filenamePath, "rb") as f:
                while chunk := f.read(2048):
                    self.transport.write(chunk)
            print("文件发送完成 !!")
        elif data_json.get("fileSave") == "ok":
            print("客户端接收文件完成")

        return super().dataReceived(data)

    def send_file(self, filename):
        try:
            self.totalBytesRead = os.path.getsize(filename)
            self.filenamePath = filename
            self.filename = str(filename).split("/")[-1]
            self.send_response({"workListener": "fileReceiverReady"})
        except FileNotFoundError:
            print(f"文件 {filename} 未找到！")
            self.send_response({"error": "File not found"})
        except Exception as e:
            print(f"发送文件时出错: {str(e)}")
            self.send_response({"error": str(e)})
        
    def send_message(self, message):
        self.transport.write(message.encode())

class EchoFactory(protocol.Factory):
    def __init__(self, newClientSignal):
        self.newClientSignal = newClientSignal

    def buildProtocol(self, addr):
        return EchoServer(self.newClientSignal)

if __name__ == "__main__":
    reactor.listenTCP(6353, EchoFactory())
    print("Server started on port 6353")
    reactor.run()
