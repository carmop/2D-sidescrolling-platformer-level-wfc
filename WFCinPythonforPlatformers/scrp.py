# import numpy as np
# import cv2 as cv
# from PIL import Image

# GAP = np.array([0,0,0,0])

# im = Image.open("images/id1.png")
# array = np.array(im)

# column = 288
# row = 160

# y_offset = 239 # make it mario's max j height

# platform_found = False
# gc = 0
# floor_height = 1110
# for x in range(row):

#     # Iterate on x direction until find a gap
#     if array[y_offset][x][3] == 0: # Gap found
#         if not platform_found:  # Increase gap size while platform is not found
#             gc +=1

#         # Check above (until sky limit is reached [224 pixels]) gap to find platform
#         for i in range(y_offset-16):
            
#             if (array[y_offset-i][x][3] != 0): # Found platform
#                 platform_found = True

#                 if(y_offset-i < floor_height): 
#                     floor_height = y_offset-i

# print("gap size", gc - 1)
# print("FloorHeight",y_offset-floor_height+1)

# print((gc-1) + ((82/5041) * ((y_offset-floor_height+1)**2)) - ((164/71) * (y_offset-floor_height+1)))


# # ------------------------------------------------------------- #

# # max jump standing -> 66 pix
# # max jump running -> 82 pix

# # jump parabola eq -> Y = - (82/5041)*(X^2) + (164/71)*X 
# # jump parabola eq set to zero -> Y + (82/5041)*(X^2) - ((164/71)*X) = 0
# # set y and x equal to point we want to check
# # To shift Y in the positive direction to acomodate for new starting height subtract `a` from Y
# # (Y-a) + (82/5041)*(X^2) - ((164/71)*X) = 0
# # To shift X in the positive direction to acomodate for new starting width subtract `b` from X (in both instances)
# # (Y-a) + (82/5041)*(X^2 - b) - ((164/71)*(X - b)) = 0
 

# def blocks():
#     """"""
    
#     tile = 16 # size of square side of tiles
#     column = 224 # 14 tiles
#     row = 160 # 10 tiles
#     max_jump = 82 # 5.125 tiles (5 tiles using floor division `//`)

#     # mid point of a tile is 7x7

#     check_y = column - max_jump

    

#     pass


# def find_alt_path():
#     """"""

#     pass


# def find_gap():
#     """"""

#     pass


# def is_inside_arc():
#     """"""

#     pass


# # [
# #     []
# #     []
# #     []
# #     []
# #  ]

# # y starts up 
# # x starts left
# # (0,0) is top left

# # [y][x]

# # x + 160
def calculates(s:tuple,e:tuple) -> int:

    # shift orign of jump parabola
    a = s[0]
    b = s[1]

    # check if the end point is inside the parabola or not
    Y = e[0]
    X = e[1]

    result = (-Y+a) - ((82/5041)*(X - b)**2) + ((164/71)*(X - b))

    return result

print(calculates((0,0),(0,0))) # SHOULD be 0

print(calculates((0,0),(160,160))) # -206

print(calculates((0,0),(20,20))) # 19

print(calculates((32,32),(20,20))) # -18

print(calculates((32,32),(50,50))) # 18

print(calculates((80,127),(80,144))) # 34

