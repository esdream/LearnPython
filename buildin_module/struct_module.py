import struct
print(struct.pack('>I', 10240099))
print(struct.pack('<I', 10240099))

def isbmp(files):
    with open(files, 'rb') as fp:
        bitOfBmp = fp.read()
        if(len(bitOfBmp) < 30):
            print('The file is not a bitmap.')
        else:
            fileInfo = struct.unpack('<ccIIIIIIHH', bitOfBmp[0:30])
            if(fileInfo[0] == b'B' and fileInfo[1] == b'M'):
                print('The size of BitMap is %s * %s, #color is %s' % (fileInfo[6], fileInfo[7], fileInfo[9]))
            else:
                print('The file is not a bitmap.')

if(__name__ == '__main__'):
    isbmp('24bitmap.bmp')
