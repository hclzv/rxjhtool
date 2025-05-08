from socketserver import TCPServer,StreamRequestHandler
import json,pydirectinput,datetime,time,psutil

class A(StreamRequestHandler):
    
    def handle(self) -> None:
        r = self.rfile.readline()
        time.sleep(1)
        print("curtime: ",datetime.datetime.now())
        if r:
            data = json.loads(r.decode())
            if data.get("shangdianInt"):
                for i in data.get("shangdianInt"):
                    pydirectinput.press(i)
            if data.get("leftclick"):
                for i in range(int(data.get("leftclick"))):
                    print("鼠标左键点击:")
                    pydirectinput.click()
                print("鼠标左键点击: 完成!")
            if data.get("english-input"):
                for i in data.get("english-input"):
                    pydirectinput.press(i)


if __name__ == "__main__":
    a = TCPServer(("",49901),A)
    print(f"server runing ..:49901")
    a.serve_forever()