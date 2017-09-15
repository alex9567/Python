import os
import time


source = r'D:\\t1'


target_dir = r'D:\\t3\\'


target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.rar'

rar_command = r'"C:\Program Files\WinRAR\WinRAR.exe" A %s %s -r' % (target,source)

if os.system(rar_command) == 0:
    print('Successful backup to',target)
else:
    print('back failed')

