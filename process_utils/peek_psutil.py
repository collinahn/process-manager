import psutil
import time


from constants.const import IGNORE_EXT

class PeekProcessPsutil:
    def __init__(self) -> None:
        self.process_status = {}

    def peek(self) -> dict[list, list]:
        for process in psutil.process_iter():
            try:
                if len(process.cmdline()) > 1:
                    self.process_status[process.pid] = ([
                        line for line in process.cmdline() if not line.startswith('-')
                        ], [file.path for file in process.open_files() if not file.path.endswith(IGNORE_EXT) and '.' in file.path]) # ( [cmd line when started], [current open files])

            except psutil.AccessDenied:
                continue
        
        return self.process_status


if __name__ == '__main__':
    from pprint import pprint
    
    start_time = time.perf_counter()

    pp = PeekProcessPsutil()
    pprint(pp.peek())

    end_time = time.perf_counter()
    print(f'{end_time - start_time}s passed')


    start_time = time.perf_counter()

    from process_utils.foreground_pids import ForegroundApp
    pp = PeekProcessPsutil()
    fa = ForegroundApp()
    print(fa.pids)
    pprint({ pid:tpl_info for pid, tpl_info in pp.peek().items() if pid in fa.pids })

    end_time = time.perf_counter()
    print(f'{end_time - start_time}s passed')

    
