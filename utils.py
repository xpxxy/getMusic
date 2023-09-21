import psutil
import win32gui
import win32con
import win32process

#获取音乐软件进程号
def getMusicPid():
    PidList = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] == 'cloudmusic.exe':
                PidList.append(proc.info['pid'])
            if proc.info['name'] == 'QQMusic.exe':
                PidList.append(proc.info['pid'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return PidList

#获取所有的窗口句柄筛选是否存在该进程
def get_all_hwnd(hwnd,mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        nID = win32process.GetWindowThreadProcessId(hwnd)
        # print(nID,win32gui.GetWindowText(hwnd))
        del nID[0]
        for abc in nID:
            try:
                pro = psutil.Process(abc).name()
            except psutil.NoSuchProcess:
            # and :
                pass
            else:
                # print(abc,win32gui.GetWindowText(hwnd))
                PIDs = getMusicPid()
                for pid in PIDs:
                    if abc == pid and win32gui.GetWindowText(hwnd)!='桌面歌词' :
                        with open('music.txt','w') as f:
                            f.write(win32gui.GetWindowText(hwnd))
                        # print("进程ID：", abc, "窗口句柄: ", hwnd, "标题: ", win32gui.GetWindowText(hwnd))
                        # print(win32gui.GetWindowText(hwnd))
                        # win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
def getMusic():
    win32gui.EnumWindows(get_all_hwnd, 0)
