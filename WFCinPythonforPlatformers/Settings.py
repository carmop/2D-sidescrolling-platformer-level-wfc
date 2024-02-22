#Controls

INTERACTIVE = True
INTERACTIVE_KEYPRESS = True
WEIGHTED = True

#Path to spritesheet
SPRITESHEET_PATH = "images/debug_sprites.png"

#Amount of tiles per level
LEVEL_LENGTH = 15
LEVEL_H = 1

#Tile sprites are 4 pixels tall and 3 pixels wide
Y_TILE = 16
X_TILE = 16

#Upscaling factor
SCALING = 10
X_SCALE = 10
Y_SCALE = 10

#Directions 
LEFT = 0
RIGHT = 1

#Tile Types:

EASY_STRAIGHT_LOW = 0
EASY_STRAIGHT_MID = 1
EASY_STRAIGHT_TOP = 2
EASY_LOW_TO_MID = 3
EASY_LOW_TO_TOP = 4
EASY_MID_TO_LOW = 5
EASY_MID_TO_TOP = 6
EASY_TOP_TO_MID = 7
EASY_TOP_TO_LOW = 8
EASY_MID_V = 9
EASY_MID_A = 10
EASY_TOP_V = 11
EASY_TOP_A = 12

MED_STRAIGHT_LOW = 13
MED_STRAIGHT_MID = 14
MED_STRAIGHT_TOP = 15
MED_LOW_TO_MID = 16
MED_LOW_TO_TOP = 17
MED_MID_TO_LOW = 18
MED_MID_TO_TOP = 19
MED_TOP_TO_MID = 20
MED_TOP_TO_LOW = 21
MED_MID_V = 22
MED_MID_A = 23
MED_TOP_V = 24
MED_TOP_A = 25

HARD_STRAIGHT_LOW = 26
HARD_STRAIGHT_MID = 27
HARD_STRAIGHT_TOP = 28
HARD_LOW_TO_MID = 29
HARD_LOW_TO_TOP = 30
HARD_MID_TO_LOW = 31
HARD_MID_TO_TOP = 32
HARD_TOP_TO_MID = 33
HARD_TOP_TO_LOW = 34
HARD_MID_V = 35
HARD_MID_A = 36
HARD_TOP_V = 37
HARD_TOP_A = 38


#Tile Sides:

LOW = 1
MID = 2
TOP = 3

"""Tile Rules (also called "adjecency" rules)

There sets of rules represent the way in which the tiles are allowed
to be put together, a.k.a which tile is allowed to be next to which tile.
"""
tileRules = {
    EASY_STRAIGHT_LOW : [LOW, LOW],
    EASY_STRAIGHT_MID : [MID, MID],
    EASY_STRAIGHT_TOP : [TOP, TOP],
    EASY_LOW_TO_MID : [LOW, MID],
    EASY_LOW_TO_TOP : [LOW, TOP],
    EASY_MID_TO_LOW : [MID, LOW],
    EASY_MID_TO_TOP : [MID, TOP],
    EASY_TOP_TO_MID : [TOP, MID],
    EASY_TOP_TO_LOW : [TOP, LOW],
    EASY_MID_V : [MID, MID],
    EASY_MID_A : [MID, MID],
    EASY_TOP_V : [TOP, TOP],
    EASY_TOP_A : [TOP, TOP],

    MED_STRAIGHT_LOW : [LOW, LOW],
    MED_STRAIGHT_MID : [MID, MID],
    MED_STRAIGHT_TOP : [TOP, TOP],
    MED_LOW_TO_MID : [LOW, MID],
    MED_LOW_TO_TOP : [LOW, TOP],
    MED_MID_TO_LOW : [MID, LOW],
    MED_MID_TO_TOP : [MID, TOP],
    MED_TOP_TO_MID : [TOP, MID],
    MED_TOP_TO_LOW : [TOP, LOW],
    MED_MID_V : [MID, MID],
    MED_MID_A : [MID, MID],
    MED_TOP_V : [TOP, TOP],
    MED_TOP_A : [TOP, TOP],

    HARD_STRAIGHT_LOW : [LOW,LOW],
    HARD_STRAIGHT_MID : [MID, MID],
    HARD_STRAIGHT_TOP : [TOP, TOP],
    HARD_LOW_TO_MID : [LOW, MID],
    HARD_LOW_TO_TOP : [LOW, TOP],
    HARD_MID_TO_LOW : [MID, LOW],
    HARD_MID_TO_TOP : [MID, TOP],
    HARD_TOP_TO_MID : [TOP, MID],
    HARD_TOP_TO_LOW : [TOP, LOW],
    HARD_MID_V : [MID, MID],
    HARD_MID_A : [MID, MID],
    HARD_TOP_V : [TOP, TOP],
    HARD_TOP_A : [TOP, TOP]


}

#Tile Weights
tileWeights = {
    EASY_STRAIGHT_LOW : 1,
    EASY_STRAIGHT_MID : 1,
    EASY_STRAIGHT_TOP : 1,
    EASY_LOW_TO_MID : 2,
    EASY_LOW_TO_TOP : 5,
    EASY_MID_TO_LOW : 2,
    EASY_MID_TO_TOP : 2,
    EASY_TOP_TO_MID : 2,
    EASY_TOP_TO_LOW : 2,
    EASY_MID_V : 2,
    EASY_MID_A : 2,
    EASY_TOP_V : 2,
    EASY_TOP_A : 2,

    MED_STRAIGHT_LOW : 1,
    MED_STRAIGHT_MID : 1,
    MED_STRAIGHT_TOP : 1,
    MED_LOW_TO_MID : 1,
    MED_LOW_TO_TOP : 1,
    MED_MID_TO_LOW : 1,
    MED_MID_TO_TOP : 1,
    MED_TOP_TO_MID : 1,
    MED_TOP_TO_LOW : 1,
    MED_MID_V : 1,
    MED_MID_A : 1,
    MED_TOP_V : 1,
    MED_TOP_A : 1,

    HARD_STRAIGHT_LOW : 1,
    HARD_STRAIGHT_MID : 1,
    HARD_STRAIGHT_TOP : 1,
    HARD_LOW_TO_MID : 1,
    HARD_LOW_TO_TOP : 1,
    HARD_MID_TO_LOW : 1,
    HARD_MID_TO_TOP : 1,
    HARD_TOP_TO_MID : 1,
    HARD_TOP_TO_LOW : 1,
    HARD_MID_V : 1,
    HARD_MID_A : 1,
    HARD_TOP_V : 1,
    HARD_TOP_A : 1 
}

tileSprites = {
    EASY_STRAIGHT_LOW : (0, 0),
    EASY_STRAIGHT_MID : (32, 0),
    EASY_STRAIGHT_TOP : (16, 0),
    EASY_LOW_TO_MID : (48, 0),
    EASY_LOW_TO_TOP : (192, 0),
    EASY_MID_TO_LOW : (64, 0),
    EASY_MID_TO_TOP : (128, 0),
    EASY_TOP_TO_MID : (112, 0),
    EASY_TOP_TO_LOW : (176, 0),
    EASY_MID_V : (96, 0),
    EASY_MID_A : (80, 0),
    EASY_TOP_V : (144, 0),
    EASY_TOP_A : (160, 0),

    MED_STRAIGHT_LOW : (0, 32),
    MED_STRAIGHT_MID : (32, 32),
    MED_STRAIGHT_TOP : (16, 32),
    MED_LOW_TO_MID : (48, 32),
    MED_LOW_TO_TOP : (192, 32),
    MED_MID_TO_LOW : (64, 32),
    MED_MID_TO_TOP : (128, 32),
    MED_TOP_TO_MID : (112, 32),
    MED_TOP_TO_LOW : (176, 32),
    MED_MID_V : (96, 32),
    MED_MID_A : (80, 32),
    MED_TOP_V : (144, 32),
    MED_TOP_A : (160, 32),
    
    HARD_STRAIGHT_LOW : (0, 64),
    HARD_STRAIGHT_MID : (32, 64),
    HARD_STRAIGHT_TOP : (16, 64),
    HARD_LOW_TO_MID : (48, 64),
    HARD_LOW_TO_TOP : (192, 64),
    HARD_MID_TO_LOW : (64, 64),
    HARD_MID_TO_TOP : (128, 64),
    HARD_TOP_TO_MID : (112, 64),
    HARD_TOP_TO_LOW : (176, 64),
    HARD_MID_V : (96, 64),
    HARD_MID_A : (80, 64),
    HARD_TOP_V : (144, 64),
    HARD_TOP_A : (160, 64),

}
