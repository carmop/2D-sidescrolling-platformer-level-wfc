import os
import numpy as np
import cv2 as cv
from PIL import Image


GAP = np.array([255,0,200,255]) # SET TO BG COLOUR!
HOLE = GAP[0]

column = 240 # value of `Y_TILE` from Settings.py
row = 160 # X_TILE value of `X_TILE` from Settings.py
tile_side = 16 # length of side of level tiles in pixels
level_length = 10 # equal to `LEVEL_LENGTH` found in Settings.py
lowest_plat = 32 # lowest platforms start 32 pix from bottom of level
maxj = 64 # max jum w/o run
height_lowest_platform = column - lowest_plat # 208

directory = '../result_images'
# directory = 'test/test_images'


def find_starting_point(array) -> tuple:
    """ """

    starting_point = 0
    
    for x in range(row):
        for y in range(16, column):
            
            if array[y][x][0] != HOLE:
                starting_point = (y,x,array[y][x]) # coordinates in Y,X format and color value
                break
        
        if starting_point != 0:
            break

    return starting_point


# def find_gap(pos) -> tuple:
#     """ """

#     gap_size = 0
#     y_pos = pos[0]
#     x_pos = pos[1]
    
#     gap_start = None

#     for x in range (x_pos, row):
#         is_gap = False
    
#         if array[y_pos][x][0] == HOLE:

#             for y in range(y_pos-maxj, y_pos): # 16 to 142 when starting at lowest plat

#                 if array[y][x][0] != HOLE:
#                     is_gap = False
#                     break
#                 else: 
#                     is_gap = True
#                     # print("!!!",y,x)
#                     if gap_start == None:
#                         for i in range(column-lowest_plat-maxj, column-lowest_plat + 1): #144 to 208
#                             if array[i][x-1][0]!= HOLE:
                                
#                                 gap_start = (i,x)
#                                 # gap_start = (pix,(((x)//16) * 16) - 1)
#                                 break
        
#         if is_gap: # Count size of gap that will be jumped
#             gap_size +=1

#     # Only return gap if it is > 1 whole tile (16 pixs)
#     # print("GSt",gap_start)
#     if gap_size > 15:

#         x_coord = gap_start[1]+gap_size # x coordinate of end of gap

#         for j in range(16, column-lowest_plat + 1): # from top of level to 32 pixels high
#             if array[j][x_coord+1][0]!= HOLE:
#                 print("END",j,gap_start[1]+gap_size)
#                 break


#         return gap_start, gap_size
#     else: 
#         return None, None


def is_gap(array, suspected_coordinate) -> bool:
    """"""

    Y = suspected_coordinate[0]
    X = suspected_coordinate[1]

    for i in range(tile_side, Y):
        if array[i][X][0] != HOLE:
            print(f"Suspected Gap at Y{Y}, X{X} was False Positive")
            return False
        else: 
            return True
    pass


def gap_coordinates(array, X:int) -> list:
    """"""

    gap_coords = []

    start_found = False
    end_found = False
    
    starting_coordinate = None
    landing_coordinate = None

    for i in range(1,(140)): # check right and left until we find starting and landing platform
        for j in range(tile_side, height_lowest_platform+1): # stop only when found lowest landing platform
            # print("*****", "X", X+i, "Y", j)
            if (array[(height_lowest_platform+tile_side)-j][X+i][0] != HOLE) and end_found is False:
                end_found = True
                landing_coordinate = ((height_lowest_platform+tile_side)-j, X+i)

                # if next tile is not empty must continue to check in order to find landing Y value
                if array[(height_lowest_platform+tile_side) - j - 1][X+i][0] != HOLE: 
                    end_found = False
        
            if (array[j][X-i][0] != HOLE) and start_found is False: # stop once we found highest star platform

                starting_coordinate = (j, X-i)
                start_found = True

            if start_found is True and end_found is True:
                break


    gap_coords.append(starting_coordinate)
    gap_coords.append(landing_coordinate)

    for item in gap_coords:
        if item == None:
            print("IMPOSSIBLE GAP LARGER THAN 8 TILES WIDE!!!!!!!!")
            exit()


    return gap_coords


def gaps(array) -> dict:
    """"""

    pitfalls = dict() # Dictionary to hold coordinates of gaps of level

    false_positives = dict()

    for i in range(level_length - 1):

        x_coordinate = 159*(i+1)

        for j in range (tile_side):
            y_coordinate = height_lowest_platform + j

            if (array[height_lowest_platform + j][x_coordinate][0] != HOLE): # check left edge for gap presence
                print(f"No Gap at Y:{y_coordinate}, X:{x_coordinate}")
                # print("a:", array[height_lowest_platform + j][x_coordinate][0])
                # if the intersection between tile is not a gap move on to next intersection

            else:
                print(f"Possible gap at Y:{y_coordinate}, X:{x_coordinate} on Right Side of Tile" )

                pitfalls[f"gapAtRightEdgeTile{i+1}"] = (height_lowest_platform,x_coordinate)
            
            if (array[height_lowest_platform + j][x_coordinate+1+i][0] != HOLE): # check right edge for gap presence
                print(f"No Gap at Y:{y_coordinate}, X:{x_coordinate+1+i}")
                break # if the intersection between tile is not a gap move on to next intersection
            
            else:
                print(f"Possible gap at Y:{y_coordinate}, X:{x_coordinate} on Left Side of Tile")

                pitfalls[f"gapAtLeftEdgeTile{i+1}"] = (height_lowest_platform,x_coordinate+1+i)

    for k in pitfalls.keys():
        # print(k)
        # print("PITFALLS",pitfalls[k])
        if is_gap(array, pitfalls[k]) == False: # check is suspected gaps are actual gaps
            false_positives[k] = pitfalls[k] # track false positives if there are any
            pitfalls.pop(k) # remove false positives

    
    return pitfalls


def is_jumpable(start:tuple, end:tuple):
    """ """

    Y = column - end[0]
    X = end[1]

    a = column - start[0]
    b = start[1]

    # Special case where the point is before the vertex of a parabola 
    x_vertex = b-(-(164/71)/(2*(82/5041)))
    
    if X <= x_vertex and Y <= (maxj+a):
        return 1 # positive number means that jump is possible

    # print("JMP",start,end)
    result = (-Y+a) - ((82/5041)*(X - b)**2) + ((164/71)*(X - b))

    if result < 0:
        print(f"UNABLE TO OVERCOME GAP AT:{start}")

    return result


def test_level(dir) -> int:
    """"""

    file_n = 0

    impossible_jmp = 0

    for f in os.listdir(dir):

        file_n += 1
        print("---------------------------")
        print(f"Analyzing Level #{file_n}: '{f}'")
        print("---------------------------")
        im = Image.open(f"{directory}/{f}")

        image_pix_array = np.array(im)
        coordinates_dict = dict()

        start = find_starting_point(image_pix_array) # returns starting point of level as tuple in (Y,X) format

        # get all gaps into a dict

        level_gaps = gaps(image_pix_array) # all gaps of level

        # for k in level_gaps:
        #     coordinates_dict[k] = gap_coordinates(level_gaps[k][1]) # pass X value from level gaps to coodinates function

        # print(coordinates_dict)

        for k in level_gaps:
            coordinates_dict[k] = gap_coordinates(image_pix_array, level_gaps[k][1])
        # print("COORDS",coordinates_dict)

        # print("Level gaps",coordinates_dict)

        for coordinate_key in coordinates_dict.keys():
            # print(coordinates_dict[coordinate_key])

            jump_start = coordinates_dict[coordinate_key][0]
            jump_end = coordinates_dict[coordinate_key][1]
            
            if is_jumpable(jump_start,jump_end) < 0:
                print(f"IMPOSSIBLE GAP FOUND IN LEVEL{file_n}: '{f}'")
                impossible_jmp += 1
                break


    return impossible_jmp, file_n


def run_tests() -> None:
    """"""

    unplayable_levels_n, level_n = test_level(directory)

    print(f"OUT OF {level_n} LEVELS, {unplayable_levels_n} JUMPS WERE IDENTIFIED AS UNPLAYABLE!")


run_tests()