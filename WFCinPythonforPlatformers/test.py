import numpy as np
import cv2 as cv
from PIL import Image


GAP = np.array([0,0,0,0])

im = Image.open("images/test_images/id4.png")
array = np.array(im)

column = 240
row = 160


lowest_plat = 32 # lowest platforms start 32 pix from bottom of level
maxj = 64 # max jum w/o run

#           [y][x]
# print(array[0][0])
# print(array[0][1])
# print(array[0][2])

# print(array[0][0])
# print(array[1][0])
# print(array[2][0])
# print(array[3][0])
# print(array)


def find_starting_point() -> tuple:
    """ """

    starting_point = 0
    
    for x in range(row):
        for y in range(16, column):
            
            if array[y][x][3] != GAP[3]:
                starting_point = (y,x,array[y][x]) # coordinates in Y,X format and color value
                break
        
        if starting_point != 0:
            break

    return starting_point


def find_gap(pos) -> tuple:
    """ """

    gap_size = 0
    y_pos = pos[0]
    x_pos = pos[1]
    
    gap_start = None

    for x in range (x_pos, row):
        is_gap = False
    
        if array[y_pos][x][3] == GAP[3]:

            for y in range(y_pos-maxj, y_pos): # 16 to 142 when starting at lowest plat

                if array[y][x][3] != GAP[3]:
                    is_gap = False
                    break
                else: 
                    is_gap = True
                    # print("!!!",y,x)
                    if gap_start == None:
                        for i in range(column-lowest_plat-maxj, column-lowest_plat + 1): #144 to 208
                            if array[i][x-1][3]!= GAP[3]:
                                
                                gap_start = (i,x)
                                # gap_start = (pix,(((x)//16) * 16) - 1)
                                break
        
        if is_gap: # Count size of gap that will be jumped
            gap_size +=1

    # Only return gap if it is > 1 whole tile (16 pixs)
    # print("GSt",gap_start)
    if gap_size > 15:

        x_coord = gap_start[1]+gap_size # x coordinate of end of gap

        for j in range(16, column-lowest_plat + 1): # from top of level to 32 pixels high
            if array[j][x_coord+1][3]!= GAP[3]:
                print("END",j,gap_start[1]+gap_size)
                break


        return gap_start, gap_size
    else: 
        return None, None


a = find_starting_point()
print("start_point",a)
b,c = find_gap(a)
print("gap start:",b,"gap size:",c)
# b = print("gap_size",find_gap(a))

def is_jumpable():
    """ """

    pass