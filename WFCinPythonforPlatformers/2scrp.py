import numpy as np
import cv2 as cv
from PIL import Image

GAP = np.array([0,0,0,0])

im = Image.open("images/id1.png")
array = np.array(im)

column = 288
row = 160

y_offset = 239 # make it mario's max j height

platform_found = False
gc = 0
floor_height = 1110
for x in range(row):

    # Iterate on x direction until find a gap
    if array[y_offset][x][3] == 0: # Gap found
        if not platform_found:  # Increase gap size while platform is not found
            gc +=1

        # Check above (until sky limit is reached [224 pixels]) gap to find platform
        for i in range(y_offset-16):
            
            if (array[y_offset-i][x][3] != 0): # Found platform
                platform_found = True

                if(y_offset-i < floor_height): 
                    floor_height = y_offset-i

print("gap size", gc - 1)
print("FloorHeight",y_offset-floor_height+1)

# Mathematical function of Mario's jump parabola used to find if the tip of platform lies within the parabola
print((gc-1) + ((82/5041) * ((y_offset-floor_height+1)**2)) - ((164/71) * (y_offset-floor_height+1)))
#     X-coor                        Y-coor                                            Y-coor



# [
#     []
#     []
#     []
#     []
#  ]

# y starts up 
# x starts left
# (0,0) is top left

# [y][x]

# x + 160