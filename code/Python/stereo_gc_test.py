#!/usr/bin/python

import sys
import cv

def findstereocorrespondence(image_left, image_right):
    # image_left and image_right are the input 8-bit single-channel images
    # from the left and the right cameras, respectively
    (r, c) = (image_left.rows, image_left.cols)
    disparity_left = cv.CreateMat(r, c, cv.CV_16S)
    disparity_right = cv.CreateMat(r, c, cv.CV_16S)
    #state = cv.CreateStereoGCState(20, 8)
    state = cv.CreateStereoGCState(20,8)
    state.minDisparity = 0
    cv.FindStereoCorrespondenceGC(image_left, image_right, disparity_left, disparity_right, state, 0)
    return (disparity_left, disparity_right)


if __name__ == '__main__':

    (l, r) = [cv.LoadImageM(f, cv.CV_LOAD_IMAGE_GRAYSCALE) for f in sys.argv[1:]]

    (disparity_left, disparity_right) = findstereocorrespondence(l, r)

    disparity_left_visual = cv.CreateMat(l.rows, l.cols, cv.CV_8U)
    cv.ConvertScale(disparity_left, disparity_left_visual, -16)
    cv.SaveImage("disparity.jpg", disparity_left_visual)
