# Copyright (2024) William Johnson
# <dev.williamj@outlook.com>
import sys
import os
import cv2 as cv

if len(sys.argv) < 4:
    print("path, widths and heights required")
    sys.exit()

p = sys.argv[1]
w = 0
h = 0
t1 = 0
t2 = 0
try:
    w = int(sys.argv[2])
    h = int(sys.argv[3])
except:
    print("cannot extract integers expected for image dimensions")
    sys.exit()
if w == 0 or h == 0:
    print("dimensions cannot be equal to zero")
    sys.exit()
if not os.path.exists(p):
    print("path parameter is invalid")
    sys.exit()
if not os.path.isdir(p):
    print("path parameter is not a directory")
    sys.exit()

for sd, d, fl in os.walk(p):
    for f in fl:
        t1 = t1 + 1
        fp = sd + os.sep + f
        try:
            i = cv.imread(fp)
            ri = cv.resize(i, (w, h))
            if cv.imwrite(fp, ri):
                t2 = t2 + 1
        except Exception as e:
            print(f"An error occurred: {e}")
            pass
print(f"{(t2/t1)*100.0}% images successfully processed")
