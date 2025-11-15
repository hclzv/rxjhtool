import pydirectinput
import time
import logging

if __name__ == "__main__":
    keys = {5:"f5",6:"f6",7:"f7"}
    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(funcName)s - %(message)s',)
    l = logging.getLogger()
    l.info("5秒后 开始执行运行!")
    time.sleep(5)
    while True:
        pydirectinput.keyDown("ctrl")
        pydirectinput.keyDown("c")
        time.sleep(1)
        pydirectinput.keyUp("c")
        pydirectinput.keyUp("ctrl")
        for k,v in keys.items():
            l.info("3秒后 开始执行下一步操作")
            time.sleep(3)
            l.info("键盘输入 %s" %v)
            pydirectinput.press(v)

        sn = 0
        while True:
            pydirectinput.press("f1")
            l.info("f1 control %s" %sn)
            time.sleep(2)
            sn += 1
            if sn == 300:
                l.info("开始执行下一轮操作")
                break
