import numpy as np
import struct

### Reading and Writing PGM Files (Greyscale Images) ###

def readpgm2(name):
# Reads a pgm file (ASCII/P2) 
# Returns a 2D array of ints with a header of metada
# Returns [[w,h], [gray], data]

    with open(name) as f:
        lines = f.readlines()
    for l in list(lines):
        if l[0] == '#':
            lines.remove(l)
    assert lines[0].strip() == 'P2' 
    arr = []
    for li in lines[1:]:
        s_li = li.split()
        i_li = list(map(lambda x: int(x), s_li))
        arr.append(i_li)
    return arr

def readpgm5(name):
# Reads a pgm file (binary/P5)
# Returns a 2D array of ints with a header of metada
# Returns [[w,h], [gray], data]

    f = open(name, "rb")
    header = []
    w=0
    h=0
    while(len(header)<3):
        temp = f.readline()
        if temp[0]==35:
            print("Comment detected in " + name)
        elif len(header)==0:
            assert (temp == b'P5\n')
            header.append(temp.decode("utf-8"))
        elif len(header)==1:
            (w, h) = [int(i.decode("utf-8")) for i in temp.split()]
            header.append([w,h])
        elif len(header)==2:
            header.append([int(temp)])

    data = []
    data.append(header[1])
    data.append(header[2])
    for y in range(h):
        row = []
        for y in range(w):
            row.append(ord(f.read(1)))
        data.append(row)
    return data

def readpgm(name):
# Reads a pgm file (binary or ascii)
# Returns a 2D array of ints with a header of metada
# Returns [[w,h], [gray], data]

    try:
        try:
            return readpgm5(name)
        except:
            return readpgm2(name)
    except:
        print("Error reading " + name)
        return

def writepgm(file_name, data):
# Writes a pgm file (binary/P5) given pgm data with header
# file_name: the path/name of the file to write to, including ".pgm" extension

    file_handle = open (file_name, 'wb')
    w = data[0][0]
    h = data[0][1]
    gray = data [1][0]
    pgm_header = f'P5\n{w} {h}\n{gray}\n'
    
    file_handle.write (bytearray (pgm_header, 'ascii')) 

    grayV = np.reshape (data[2:], w*h)

    grayB = struct.pack ('%sB' % len(grayV), *grayV)
    file_handle.write(grayB)
    file_handle.close()
    return

### Reading and Writing PPM Files (Full-Color Images) ###

def readppm3(name):
# Reads a ppm file (ASCII/P3) 
# Returns a 2D array of ints with a header of metada
# Returns [[w,h], [gray], data]

    with open(name) as f:
        lines = f.readlines()
    for l in list(lines):
        if l[0] == '#':
            lines.remove(l)
    assert lines[0].strip() == 'P3' 
    arr = []
    for li in lines[1:]:
        s_li = li.split()
        i_li = list(map(lambda x: int(x), s_li))
        arr.append(i_li)
    return arr

def readppm6(name):
# Reads a pgm file (binary/P6)
# Returns a 2D array of ints with a header of metada
# Returns [[w,h], [gray], data]

    f = open(name, "rb")
    header = []
    w=0
    h=0
    while(len(header)<3):
        temp = f.readline()
        if temp[0]==35:
            print("Comment detected in " + name)
        elif len(header)==0:
            assert (temp == b'P6\n')
            header.append(temp.decode("utf-8"))
        elif len(header)==1:
            (w, h) = [int(i.decode("utf-8")) for i in temp.split()]
            header.append([w,h])
        elif len(header)==2:
            header.append([int(temp)])

    data = []
    data.append(header[1])
    data.append(header[2])
    for y in range(h):
        row = []
        for y in range(3*w):
            row.append(ord(f.read(1)))
        data.append(row)
    return data

def readppm(name):
# Reads a ppm file (binary or ascii)
# Returns a 2D array of ints with a header of metada
# Returns [[w,h], [gray], data]

    try:
        try:
            return readppm6(name)
        except:
            return readppm3(name)
    except:
        print("Error reading " + name)
        return
    
def writeppm(file_name, data):
# Writes a ppm file (binary/P6) given ppm data with header
# file_name: the path/name of the file to write to, including ".ppm" extension

    file_handle = open (file_name, 'wb')
    w = data[0][0]
    h = data[0][1]
    gray = data [1][0]
    pgm_header = f'P6\n{w} {h}\n{gray}\n'
    
    file_handle.write (bytearray (pgm_header, 'ascii')) 

    grayV = np.reshape (data[2:], 3*w*h)

    grayB = struct.pack ('%sB' % len(grayV), *grayV)
    file_handle.write(grayB)
    file_handle.close()
    return
