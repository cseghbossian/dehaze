# Utility Functions

def convertHSV(r, g, b):
# Converts a color from the RGB color model to the HSV color model
# r, g, b values should be in range [0,255]
# Returns a triple of floats in range [0,1] corresponding to (h,s,v)

    rr = r/255
    gg = g/255
    bb = b/255
    maxx = max(rr,gg,bb)
    minn = min(rr,gg,bb)
    delt = maxx-minn
    
    # hue 
    if delt == 0:
        h = 0
    elif maxx == rr:
        h = (((gg-bb)/delt) % 6) / 6
    elif maxx == gg:
        h = (((bb-rr)/delt) + 2) / 6
    else: # maxx == bb
        h = (((rr-gg)/delt) + 4) / 6

    # saturation
    if maxx == 0:
        s = 0
    else:
        s = delt/maxx
        
    # value
    v = maxx
    
    return (h,s,v)

def convertRGB(h, s, v):
# Converts a color from the HSV color model to the RGB color model
# h, s, v values should be in range [0,1]
# Returns a triple of ints in range [0,255] ; (r,g,b)

    H = h*360
    c = v*s
    abss = ((H/60) % 2) - 1
    x = c * (1 - abs(abss))
    m = v - c
    
    if H < 60:
        (rr,gg,bb) = (c,x,0)
    elif H < 120:
        (rr,gg,bb) = (x,c,0)
    elif H < 180:
        (rr,gg,bb) = (0,c,x)
    elif H < 240:
        (rr,gg,bb) = (0,x,c)
    elif H < 300:
        (rr,gg,bb) = (x,0,c)
    else: # H < 360:
        (rr,gg,bb) = (c,0,x)
        
    r = round((rr+m) * 255)
    g = round((gg+m) * 255)
    b = round((bb+m) * 255)
    
    return (r,g,b)

def padded_data(data, d):
# Pads a matrix with infinities and returns a new 2d array
# d = number infinities before and after each row/col
# data = pgm data including header metadata

    padded = []
    dimX = data[0][0]
    #create row of infinity
    inf = float("inf")
    inf_row = [inf] * (d + dimX + d)
    
    for _ in range(d):
        padded.append(inf_row)
    
    for r in data[2:]:
        row = []
        for _ in range(d):
            row.append(inf)
        for c in r:
            row.append(c)
        for _ in range(d):
            row.append(inf)
        padded.append(row)
        
    for _ in range(d):
        padded.append(inf_row)
        
    return padded

def find_neighbors(p, x, y, n):
# Returns the values of the neighbors of a pixel
# p = padded data
# x,y is the pixel whose neighbors are being calculated
# n is the dimension of the square neighborhood
    
    assert n%2 == 1 and n >= 3
    neighbors = []
    dist = int((n-1)/2)
    for i in range(x-dist, x+dist+1): #range(0, )
        for j in range(y-dist, y+dist+1):
            neighbors.append(p[i][j])
    return neighbors

def min_filt(data, n): 
# Applies a minimum filter onto the image
# data = pgm data including header metadata
# Filter size is nxn
# Returns data of the new greyscale image including metadata

    assert n%2 == 1 and n >= 3
    d = int((n-1)/2)
    p = padded_data(data, d)
    
    new_data = []
    new_data.append(data[0])
    new_data.append(data[1])
    for i,r in enumerate(p[d:(0-d)]):
        row = []
        for j,c in enumerate(r[d:(0-d)]):
            neighbors = find_neighbors(p, i+d, j+d, n)
            minn = min(neighbors)
            row.append(minn)
        new_data.append(row)
    return new_data

def scale_data(data, L):
# Scales data to the range [0,L-1] where L = number of gray levels
# data = pgm data including header metadata
# Returns data of the scaled image including metadata
    
    minv = min([min(d) for d in data[2:]])
    shft = []
    for r in data[2:]:
        row = []
        for c in r:
            row.append(c-minv)
        shft.append(row)
    maxv = max([max(d) for d in shft])
    
    scale = []
    scale.append(data[0])
    scale.append(data[1])
    for r in shft:
        row = []
        for c in r:
            if(L==1):
                a = c/maxv
            else:
                fact = (L+1)/maxv
                a = int(c*fact)
                if a>L: 
                    a=L
            row.append(a)
        scale.append(row)
    return scale
