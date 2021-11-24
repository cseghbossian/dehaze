import numpy as np 
from pylab import *
import math 
import struct
import heapq 
from scipy import signal as sig 

import util

def deep_points(dmap, p):
# Finds the indices of the deepest values in a depth map
# Deepest points determined by lowest values
# dmap: a 2D array representing the depth pgm of an image, incl. header metadata
# p: a decimal indicating which top percentile of points to return
# e.g. p=0.1 returns the top 0.1% deepest points
# Returns a list of point indices (x,y)

    assert p <= 100
    w = dmap[0][0]
    h = dmap[0][1]
    
    n = w*h # total number of pixels
    pp  = int(n * p / 100) # number of pixels to return
    
    # heapq is by default a min heap
    heap = [] 
    for i,r in enumerate(dmap[2:]):
        for j,c in enumerate(r):
            if(len(heap) <= pp):
                heapq.heappush(heap, (c,(i,j)))
            else:
                # heap[0][0] = min value
                if c > heap[0][0]:
                    heapq.heapreplace(heap, (c,(i,j)))
                    
    points = []
    for (val,point) in heapq.nlargest(pp, heap):
        points.append(point)
    return points
    
def est_atm_light(dmap, data):
# Given an image and its depth map, finds the value of atmospheric light (r,g,b)
# dmap: a 2D array representing the depth pgm of an image, incl. header metadata
# data: a 2D array representing the ppm of an image, incl. header metadata

    deep =  deep_points(dmap, 0.1)
    maxval = 0
    maxx = (0,0,0)
    for (x,y) in deep:
        r = data[x+2][3*y]
        g = data[x+2][(3*y)+1]
        b = data[x+2][(3*y)+2]
        i = (r+g+b)/3
        
        if i>maxval: 
            maxval = i
            maxx=(r,g,b)
    return maxx

def raw_depth_map(data):
# Finds the raw depth map of the given image
# data: a 2D array representing the ppm of an image, incl. header metadata
# Returns a 2D array representing the raw depth pgm of an image, incl. header metadata

    w = data[0][0]
    h = data[0][1]
    lvls = data[1][0]

    dmap = []
    dmap.append(data[0])
    dmap.append(data[1])
    
    # linear coeffs from study
    th0 = 0.121779
    th1 = 0.959710
    th2 = -0.780245
    sigma = 0.041337
    
    # random normal distribution
    eps = (np.random.normal(0, sigma, size=(h,w))).tolist()
    
    for r in range(h):
        row = []
        for c in range(w):
            rr = data[r+2][3*c]
            gg = data[r+2][(3*c)+1]
            bb = data[r+2][(3*c)+2]
            (_,s,v) = util.convertHSV(rr,gg,bb)
            # calculate depth
            d = th0 + (th1 * v) + (th2 * s) + eps[r][c]
            row.append(d)
        dmap.append(row)
        
    return util.scale_data(dmap, 255)

def guided_filt(guide, img, r, eps):
# Applies a guided image filter onto the image
# img, guide = pgm data including header metadata
# r = dimension of the guided image filter
# Returns data of the new greyscale image including metadata

# Code taken from https://github.com/jacob5412
# Algorithm from "Guided Image Filtering" by Kaiming He et al

    w = img[0][0]
    h = img[0][1]
    I = np.array(guide[2:])
    P = np.array(img[2:])
    window = np.ones((r, r)) / (r * r)

    meanI = sig.convolve2d(I, window, mode="same")
    meanP = sig.convolve2d(P, window, mode="same")

    corrI = sig.convolve2d(I * I, window, mode="same")
    corrIP = sig.convolve2d(I * P, window, mode="same")

    varI = corrI - meanI * meanI
    covIP = corrIP - meanI * meanP
    a = covIP / (varI + e)
    b = meanP - a * meanI

    meana = sig.convolve2d(a, window, mode="same")
    meanb = sig.convolve2d(b, window, mode="same")

    q = meana * I + meanb
    
    Q = q.astype(float).tolist()
    
    # add metadata 
    Q.insert(0, img[1])
    Q.insert(0, img[0])
    return Q

def final_depth_map(raw):
# Restores the given raw depth map
# raw: a 2D array representing the raw depth pgm of an image, incl. header metadata
# Returns a 2D array representing the final, restored depth pgm of an image, incl. header metadata
 
    # filter size for min filter:
    n = 15
    # radius for guided filter:
    r = 8
    # regularization for edge detection
    eps = 0.1
    
    # apply min filter
    minn = util.min_filt(raw, n)
    
    # apply guided image filter
    gf = guided_filt(raw, minn, r, eps)
    
    # scale
    final = util.scale_data(gf, 1)
    return final

def restore_img(data, dmap):
# Dehazes the given image 
# data: a 2D array representing the ppm of an image, incl. header metadata
# dmap: a 2D array representing the depth pgm of an image, incl. header metadata
# Returns a 2D array representing the ppm of the restored image, incl. header metadata
    beta = 1.0

    w,h = data[0]
    img = []
    img.append(data[0])
    img.append(data[1])
    
    A = est_atm_light(dmap, data)
    A_arr = [A * w] * h
    print("Atmospheric Light: " + str(A))

    for i,r in enumerate(data[2:]):
        row = []
        for j,c in enumerate(r):
            # index in depth map
            jj = int(j/3)
            
            # find transmission, t(x)
            d_x = dmap[i+2][jj]
            e = math.e
            t = math.pow(e, (-beta*d_x))
            t_x = min(max(t, 0.1), 0.9)
            j_x = ((c - A_arr[i][j]) / t_x) + A_arr[i][j]
            row.append(j_x)
        img.append(row)
    
    return util.scale_data(img, 255)