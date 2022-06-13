from win32gui import GetWindowText, GetForegroundWindow


class FocusedWindow:

    def get_info(self):
        try:
            return GetWindowText(GetForegroundWindow())
        except Exception:
            return '정보 없음'

if __name__ == '__main__':

    fw = FocusedWindow()
    print(fw.get_info())

    
    import win32gui
    import win32process
    import win32pdhutil
    import wmi

    procs = wmi.WMI().Win32_Process()

    pycwnd = win32gui.GetForegroundWindow()
    tid, pid = win32process.GetWindowThreadProcessId(pycwnd)

    for proc in procs:
        if proc.ProcessId == pid:
            print('pid', pid)
            print('exec', proc.ExecutablePath)
            print('title', win32gui.GetWindowText(pycwnd))