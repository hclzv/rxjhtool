import win32gui
import win32process
import win32api
import win32con
from win32con import PROCESS_QUERY_INFORMATION, PROCESS_VM_READ
import time
#conda install pywin32 -c conda-forge
def list_windows_info():
    """
    列出当前用户会话中所有可见的顶级窗口的详细信息。
    """
    windows_info = []

    def enum_windows_callback(hwnd, extra):
        """
        EnumWindows的回调函数，用于收集窗口信息。
        """
        # 排除不可见的窗口（通常是最小化、隐藏或系统内部窗口）
        if not win32gui.IsWindowVisible(hwnd):
            return True

        # 获取窗口标题
        window_title = win32gui.GetWindowText(hwnd)
        # 获取窗口类名
        window_class = win32gui.GetClassName(hwnd)

        # 过滤掉一些不重要的或没有标题的系统窗口
        # 例如，"Program Manager" (桌面), "Default IME" 等
        if not window_title and window_class not in ["WorkerW", "Progman", "Shell_TrayWnd", "IME", "Default IME"]:
            # 即使没有标题，如果它不是常见的系统窗口，也可能是一个有效的应用窗口
            # 但为了简洁，我们通常关注有标题的窗口
            pass
        
        # 确保窗口有标题，或者不是一些常见的系统/辅助窗口
        if window_title or (window_class not in ["WorkerW", "Progman", "Shell_TrayWnd"]):
            # 获取窗口的线程ID和进程ID
            thread_id, process_id = win32process.GetWindowThreadProcessId(hwnd)
            
            process_name = "<未知进程>"
            try:
                # 获取进程句柄，需要PROCESS_QUERY_INFORMATION和PROCESS_VM_READ权限
                # 注意：某些系统进程可能无法获取权限，导致OpenProcess失败
                h_process = win32api.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, process_id)
                # 获取进程的可执行文件路径
                process_path = win32process.GetModuleFileNameEx(h_process, 0)
                # 从路径中提取进程名
                process_name = win32api.GetFileVersionInfo(process_path, '\\StringFileInfo\\040904B0\\FileDescription')
                if not process_name: # 如果FileDescription为空，则取文件名
                     process_name = process_path.split('\\')[-1]
                
                win32api.CloseHandle(h_process) # 关闭进程句柄
            except Exception as e:
                # print(f"无法获取PID {process_id} 的进程信息: {e}")
                pass # 忽略错误，继续处理下一个窗口

            windows_info.append({
                "hwnd": hwnd,
                "title": window_title if window_title else "[无标题]",
                "class_name": window_class,
                "pid": process_id,
                "process_name": process_name,
                "is_visible": True # 已经通过IsWindowVisible过滤
            })
        return True # 继续枚举下一个窗口

    win32gui.EnumWindows(enum_windows_callback, None)
    return windows_info

if __name__ == "__main__":
    # print("正在列出所有用户的窗口 (仅限当前用户会话的顶级窗口)...")
    # print("-" * 60)

    # all_windows = list_windows_info()

    # if all_windows:
    #     for window in all_windows:
    #         print(f"HWND: {window['hwnd']:<10} | PID: {window['pid']:<6} | 进程名: {window['process_name']:<30} | 类名: {window['class_name']:<25} | 标题: {window['title']}")
    # else:
    #     print("未找到任何可见的窗口。")

    # print("-" * 60)
    # print("注意：")
    # print("1. '所有用户的窗口'在这里特指当前登录用户会话中的顶级窗口。")
    # print("2. 脚本可能无法获取所有进程的名称，特别是对于一些系统服务或权限受限的进程。")
    # print("3. 如果需要列出所有用户会话的窗口，则需要更高的权限和更复杂的API调用（如WTSQuerySessionInformation），这超出了pywin32的直接范围。")
    # print("4. Windows 7 上 UAC 对此脚本的影响较小，但在更现代的Windows版本上，部分操作可能需要管理员权限。")

    hwnd = win32gui.FindWindow(None, "无标题 - Notepad")
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.1)  # 确保窗口获得焦点

    # # 按下 Ctrl
    # win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    # # 按下 V
    # win32api.keybd_event(ord('V'), 0, 0, 0)
    # # 松开 V
    # win32api.keybd_event(ord('V'), 0, win32con.KEYEVENTF_KEYUP, 0)
    # # 松开 Ctrl
    # win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32gui.PostMessage(hwnd, win32con.WM_CHAR, ord('A'), 0)

    # 或者发送键盘消息（不一定被处理）
    win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, ord('A'), 0)
    win32gui.PostMessage(hwnd, win32con.WM_KEYUP, ord('A'), 0)