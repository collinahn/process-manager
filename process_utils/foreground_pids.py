import subprocess

class ForegroundApp:
    def __init__(self) -> None:
        self.foreground_pids = []
        self.get_foreground_app_pid()

    @property
    def pids(self) -> list:
        return self.foreground_pids

    def get_foreground_app_pid(self) -> list[int]:

        p: subprocess.Popen = self._powershell_result()

        for line in p.stdout:
            if line.rstrip():
                # only print lines that are not empty
                # decode() is necessary to get rid of the binary string (b')
                # rstrip() to remove `\r\n`
                possible_pid = line.decode().rstrip()
                try:
                    self.pids.append(int(possible_pid))
                except ValueError:
                    continue

    def _powershell_result(self) -> subprocess.Popen:
        return subprocess.Popen(
            ["powershell.exe", "Get-Process | where {$_.mainWindowTItle} | select id"], 
            stdout=subprocess.PIPE
        )


if __name__ == '__main__':
    fa = ForegroundApp()
    print(fa.pids)