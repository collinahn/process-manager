'''
wmi object example
instance of Win32_Process
{
        Caption = "conhost.exe";
        CommandLine = "\\??\\C:\\WINDOWS\\system32\\conhost.exe 0x4";
        CreationClassName = "Win32_Process";
        CreationDate = "20220605173008.208911+540";
        CSCreationClassName = "Win32_ComputerSystem";
        CSName = "DESKTOP";
        Description = "conhost.exe";
        ExecutablePath = "C:\\WINDOWS\\system32\\conhost.exe";
        Handle = "21884";
        HandleCount = 104;
        KernelModeTime = "156250";
        MaximumWorkingSetSize = 1380;
        MinimumWorkingSetSize = 200;
        Name = "conhost.exe";
        OSCreationClassName = "Win32_OperatingSystem";
        OSName = "Microsoft Windows 11 Education|C:\\WINDOWS|\\Device\\Harddisk0\\Partition3";
        OtherOperationCount = "77";
        OtherTransferCount = "4076";
        PageFaults = 2916;
        PageFileUsage = 5492;
        ParentProcessId = 25192;
        PeakPageFileUsage = 5504;
        PeakVirtualSize = "2203422437376";
        PeakWorkingSetSize = 11320;
        Priority = 8;
        PrivatePageCount = "5623808";
        ProcessId = 21884;
        QuotaNonPagedPoolUsage = 8;
        QuotaPagedPoolUsage = 123;
        QuotaPeakNonPagedPoolUsage = 8;
        QuotaPeakPagedPoolUsage = 124;
        ReadOperationCount = "0";
        ReadTransferCount = "0";
        SessionId = 1;
        ThreadCount = 4;
        UserModeTime = "0";
        VirtualSize = "2203422437376";
        WindowsVersion = "10.0.22000";
        WorkingSetSize = "11591680";
        WriteOperationCount = "0";
        WriteTransferCount = "0";
};
'''


import wmi
import psutil


WMI = wmi.WMI()

proc_list = WMI.Win32_Process()

for proc in proc_list:
    with open('./test_wmi.txt', 'a', encoding='utf-8') as f:
        print(proc)
        f.write(f'{proc}/n')

    if proc.CommandLine:
        print(proc.CommandLine)