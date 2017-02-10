import os, time
def print_fileinfo(file_str):
    fileinfo = os.stat(file_str)
    time_ele = [ele for ele in time.localtime(fileinfo.st_ctime)]
    print('%d月 %d %d:%d %s' % (time_ele[1], time_ele[2], time_ele[3], time_ele[4], file_str))

if __name__ == '__main__':
    [print_fileinfo(filename) for filename in os.listdir('.')]
