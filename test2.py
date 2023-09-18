import psutil
import win32gui
import win32con
import win32process

find_pid = int(input('请输入pid: '))


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        nID = win32process.GetWindowThreadProcessId(hwnd)
        # print(nID,win32gui.GetWindowText(hwnd))
        del nID[0]
        for abc in nID:
            try:
                pro = psutil.Process(abc).name()
            except psutil.NoSuchProcess:
                pass
            else:
                # print(abc,win32gui.GetWindowText(hwnd))          
                if abc == find_pid:
                    print("进程ID：", abc, "窗口句柄: ", hwnd, "标题: ", win32gui.GetWindowText(hwnd))
                    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)


win32gui.EnumWindows(get_all_hwnd, 0)