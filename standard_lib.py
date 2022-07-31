Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.platform
'win32'
>>> print(sys.version)
3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)]
>>> import os
>>> os.getcwd()
'C:\\Users\\64testlab\\AppData\\Local\\Programs\\Python\\Python37'
>>> os.environ
environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\64testlab\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': '64TESTLAB-PC', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'FP_NO_HOST_CHECK': 'NO', 'GOPATH': 'C:\\Users\\64testlab\\go', 'HOME': 'C:\\Users\\64testlab', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\64testlab', 'LOCALAPPDATA': 'C:\\Users\\64testlab\\AppData\\Local', 'LOGONSERVER': '\\\\64TESTLAB-PC', 'NUMBER_OF_PROCESSORS': '4', 'OS': 'Windows_NT', 'PATH': 'C:\\Users\\64testlab\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\pywin32_system32;C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\Users\\64testlab\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\;C:\\Users\\64testlab\\AppData\\Local\\Programs\\Python\\Python37\\;C:\\Program Files\\Broadcom\\Broadcom 802.11 Network Adapter\\Driver;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\ATI Technologies\\ATI.ACE\\Core-Static;D:\\Git\\cmd;C:\\Program Files\\dotnet\\;D:\\flutter\\bin;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;D:\\Enigma-Course\\Java\\SpringBoot\\apache-maven-3.8.5\\bin;D:\\Xamapp;D:\\Node;D:\\Enigma-Course\\React\\react-devtools;C:\\Program Files\\Go\\bin;C:\\Users\\64testlab\\Anaconda3;C:\\Users\\64testlab\\Anaconda3\\Scripts;C:\\Users\\64testlab\\Anaconda3\\Library\\bin;C:\\Users\\64testlab\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\;C:\\Users\\64testlab\\AppData\\Local\\Programs\\Python\\Python37\\;C:\\Users\\64testlab\\AppData\\Roaming\\npm\\dotnet;D:\\VSCode\\bin;D:\\flutter\\bin;C:\\Program Files\\Java\\jdk1.8.0_181\\bin;D:\\Enigma-Course\\Java\\SpringBoot\\apache-maven-3.8.5\\bin;D:\\Xamapp;D:\\Node;D:\\Enigma-Course\\React\\react-devtools;D:\\PyCharm Community Edition 2022.1.1\\bin;;C:\\Users\\64testlab\\go\\bin', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'AMD64 Family 22 Model 0 Stepping 1, AuthenticAMD', 'PROCESSOR_LEVEL': '22', 'PROCESSOR_REVISION': '0001', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM COMMUNITY EDITION': 'D:\\PyCharm Community Edition 2022.1.1\\bin;', 'ROBOTINOVIEW2_DIR': 'C:\\Program Files (x86)\\Didactic\\RobotinoView2', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMFOLDER_OMRON': 'C:\\Windows\\SysWOW64\\Omron\\', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\64TEST~1\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\64TEST~1\\AppData\\Local\\Temp', 'USERDOMAIN': '64testlab-PC', 'USERNAME': '64testlab', 'USERPROFILE': 'C:\\Users\\64testlab', 'VBOX_HWVIRTEX_IGNORE_SVM_IN_USE': '1', 'WINDIR': 'C:\\Windows', 'WINDOWS_TRACING_FLAGS': '3', 'WINDOWS_TRACING_LOGFILE': 'C:\\BVTBin\\Tests\\installpackage\\csilogfile.log'})
>>> os.getenv('HOME')
'C:\\Users\\64testlab'
>>> import datetime
>>> datetime.date.today()
datetime.date(2022, 6, 9)
>>> datetine.date.today().day
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    datetine.date.today().day
NameError: name 'datetine' is not defined
>>> datetime.date.today().day
9
>>> datetime.date.today().month
6
>>> datetime.date.today().year
2022
>>> datetime.date.isoformat(datetime.date.today())
'2022-06-09'
>>> import time
>>> time.strftime("%H:%M")
'11:35'
>>> time.strftime("%A %p")
'Thursday AM'
>>> import html
>>> html.escape("This HTML fragment contains a <script>script</script> tag.")
'This HTML fragment contains a &lt;script&gt;script&lt;/script&gt; tag.'
>>> html.unescape("I &hearts; Python's &lt;standard library&gt;.")
"I ♥ Python's <standard library>."
>>> 