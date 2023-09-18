import psutil
import win32gui
import win32con
import win32process
#获取音乐软件的PID
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

#通过PID 查询窗口名称
# def get_window_titles_by_pids(pid_list):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindow(hwnd, win32con.GW_OWNER) == 0:
            window_pid = win32process.GetWindowThreadProcessId(hwnd)
            if window_pid in pid_list:
                hwnds[window_pid] = hwnd

        return True

    hwnds = {}
    win32gui.EnumWindows(callback, hwnds)

    window_titles = []
    for pid in pid_list:
        hwnd = hwnds.get(pid)
        if hwnd:
            window_title = win32gui.GetWindowText(hwnd)
            window_titles.append(window_title)
        else:
            window_titles.append(None)

    return window_titles

# 使用示例
PIDs = getMusicPid()  # 将这里替换为你要查询的PID列表
# for i in PIDs:
#     process_name = psutil.Process(i).name()
#     print(process_name)

# window_titles = get_window_titles_by_pids(pid_list_to_query)

# for pid, window_title in zip(pid_list_to_query, window_titles):
#     if window_title:
#         print(f"PID {pid} window is :{window_title}")
#     else:
#         print(f"cantfind {pid} cant find")
    
    