"""Settings for dedfining the tiles and anxiety curve use in generation.

This file holds the values used by the Pygame library to define where
the tiles that should be displayed are located and their respective metadata:

- Tile dimentions
- Weights
- Tile difficulties
- Tile types
"""


"""Anxiety Curve Value List

This list defines where tiles of a certain difficulty must be placed in the level.
If the level size (LEVEL_LENGTH variable) changes 
the size of this list must be changed as well.
"""
# AC = [0,0,0,0,0,0,0,0,0,0] 
# AC = [0,1,0,1,0,1,0,1,0,1] # Alternating EASY and MEDIUM difficulty 
# AC = [1,1,1,1,1,1,1,1,1,1]
AC = [0,0,0,1,1,1,1,2,2,2] # Rising difficulty
# AC = [0,1,1,1,2,2,1,1,1,0] # Peak difficult at center of level
# AC = [2,2,0,0,0,0,0,0,2,2] # `Valley` difficulty
# AC = [2,2,2,2,2,2,2,2,2,2]

#Paths to spritesheet
# SPRITESHEET_PATH = "images/tiles/SMB_Sprites_w_Background.png" # Sprites including enemies 
# SPRITESHEET_PATH = "images/tiles/SMB_SPrites_NoEnemies_BlackBg.png" # Black BG
# SPRITESHEET_PATH = "images/tiles/ALLSPRITES+_NoEnemies_PinkBG.png" # Pink BG
SPRITESHEET_PATH = "images/tiles/ALLSPRITES+_BlueBG.png" # No BG

#Amount of tiles per level
LEVEL_LENGTH = 10

# SHOULD REMAIN 1 WHEN GENERATING 2D SIDE SCROLLING PLATFORMER LEVELS
# CURRENTLY, THIS IMPLEMENTATION DOES NOT SUPPORT ANY OTHER VALUE FOR THIS VARIABLE
LEVEL_H = 1

#Tile sprites are y pixels tall and x pixels wide
Y_TILE = 240
X_TILE = 160

#Upscaling factor
SCALING = 1
X_SCALE = 1
Y_SCALE = 1

#Directions 
LEFT = 0
RIGHT = 1

# Difficulty Types:
EASY = 0 # Tiles that have no way to harm the player
MEDIUM = 1 # Tiles that have total gaps <= 4 tiles wide
HARD = 2 # Tiles that have total gaps >=5 tiles wide

#Tile Edge Values/Tile Side Values:
LOW = 2 # Represents floor height of 2, 3, 4, 5, 6 (starting a min floor, which is 2, and going up by 4 tiles, which is Marios max jump height w/o run-up)
MID = 7 # 7, 8, 9, 10
TOP = 11 # 11, 12, 13, 14


"""Tile Types 

And id that describes each individual tile so that 
they can be reffered to during collapse and constrain.
"""
TILE_001 = 1 # Level 1-3
TILE_002 = 2
TILE_003 = 3
TILE_004 = 4
TILE_005 = 5
TILE_006 = 6
TILE_007 = 7
TILE_008 = 8
TILE_009 = 9 
TILE_010 = 10
TILE_011 = 11
TILE_012 = 12 # Level 2-1
TILE_013 = 13
TILE_014 = 14
TILE_015 = 15
TILE_016 = 16
TILE_017 = 17
TILE_018 = 18
TILE_019 = 19
TILE_020 = 20
TILE_021 = 21
TILE_022 = 22
TILE_023 = 23
TILE_024 = 24
TILE_025 = 25
TILE_026 = 26
TILE_027 = 27 
TILE_028 = 28 # Level 2-3
TILE_029 = 29
TILE_030 = 30
TILE_031 = 31
TILE_032 = 32
TILE_033 = 33
TILE_034 = 34
TILE_035 = 35
TILE_036 = 36
TILE_037 = 37
TILE_038 = 38 
TILE_039 = 39
TILE_040 = 40 # Level 3-1
TILE_041 = 41
TILE_042 = 42
TILE_043 = 43
TILE_044 = 44
TILE_045 = 45
TILE_046 = 46
TILE_047 = 47
TILE_048 = 48
TILE_049 = 49
TILE_050 = 50
TILE_051 = 51
TILE_052 = 52
TILE_053 = 53 # Level 3-3
TILE_054 = 54
TILE_055 = 55
TILE_056 = 56
TILE_057 = 57
TILE_058 = 58
TILE_059 = 59
TILE_060 = 60
TILE_061 = 61
TILE_062 = 62
TILE_063 = 63 # Level 4-1
TILE_064 = 64
TILE_065 = 65
TILE_066 = 66
TILE_067 = 67
TILE_068 = 68
TILE_069 = 69
TILE_070 = 70 # Level 4-2
TILE_071 = 71
TILE_072 = 72
TILE_073 = 73 # Level 4-3
TILE_074 = 74
TILE_075 = 75
TILE_076 = 76
TILE_077 = 77
TILE_078 = 78
TILE_079 = 79
TILE_080 = 80 # Level 5-1
TILE_081 = 81
TILE_082 = 82
TILE_083 = 83
TILE_084 = 84
TILE_085 = 85
TILE_086 = 86
TILE_087 = 87
TILE_088 = 88
TILE_089 = 89
TILE_090 = 90 # Level 5-2
TILE_091 = 91
TILE_092 = 92
TILE_093 = 93
TILE_094 = 94
TILE_095 = 95
TILE_096 = 96
TILE_097 = 97
TILE_098 = 98
TILE_099 = 99
TILE_100 = 100
TILE_101 = 101
TILE_102 = 102 # Level 6-1
TILE_103 = 103
TILE_104 = 104
TILE_105 = 105
TILE_106 = 106
TILE_107 = 107
TILE_108 = 108
TILE_109 = 109
TILE_110 = 110 # Level 6-2
TILE_111 = 111
TILE_112 = 112
TILE_113 = 113
TILE_114 = 114
TILE_115 = 115
TILE_116 = 116
TILE_117 = 117
TILE_118 = 118
TILE_119 = 119
TILE_120 = 120
TILE_121 = 121
TILE_122 = 122
TILE_123 = 123 # Level 6-3
TILE_124 = 124
TILE_125 = 125
TILE_126 = 126
TILE_127 = 127
TILE_128 = 128
TILE_129 = 129
TILE_130 = 130
TILE_131 = 131 # Level 7-1
TILE_132 = 132
TILE_133 = 133
TILE_134 = 134
TILE_135 = 135
TILE_136 = 136
TILE_137 = 137
TILE_138 = 138
TILE_139 = 139
TILE_140 = 140 # Level 7-3
TILE_141 = 141
TILE_142 = 142
TILE_143 = 143
TILE_144 = 144
TILE_145 = 145
TILE_146 = 146
TILE_147 = 147 # Level 8-1
TILE_148 = 148
TILE_149 = 149
TILE_150 = 150
TILE_151 = 151
TILE_152 = 152
TILE_153 = 153
TILE_154 = 154
TILE_155 = 155
TILE_156 = 156
TILE_157 = 157
TILE_158 = 158
TILE_159 = 159
TILE_160 = 160
TILE_161 = 161
TILE_162 = 162
TILE_163 = 163
TILE_164 = 164
TILE_165 = 165
TILE_166 = 166
TILE_167 = 167 # Level 8-2
TILE_168 = 168
TILE_169 = 169
TILE_170 = 170
TILE_171 = 171
TILE_172 = 172
TILE_173 = 173
TILE_174 = 174
TILE_175 = 175
TILE_176 = 176
TILE_177 = 177
TILE_178 = 178
TILE_179 = 179
TILE_180 = 180 # Level 8-3
TILE_181 = 181
TILE_182 = 182
TILE_183 = 183
TILE_184 = 184
TILE_185 = 185

#Tile Duplicates:
TILE_005D = 5
TILE_015D = 15
TILE_017D = 17
TILE_019D = 19
TILE_020D = 20
TILE_025D = 25
TILE_026D = 26
TILE_040D = 40
TILE_046D = 46
TILE_049D = 49
TILE_054D = 54
TILE_055D = 55
TILE_056D = 56
TILE_057D = 57
TILE_060D = 60
TILE_071D = 71
TILE_072D = 72
TILE_074D = 74
TILE_074DD = 74
TILE_076D = 76
TILE_076DD = 76
TILE_089D = 89
TILE_091D = 91
TILE_094D = 94
TILE_095D = 95
TILE_096D = 96
TILE_103D = 103
TILE_110D = 110
TILE_114D = 114
TILE_115D = 115
TILE_117D = 117
TILE_118D = 118
TILE_120D = 120
TILE_120DD = 120
TILE_120DDD = 120
TILE_125D = 125
TILE_128D = 128
TILE_131D = 131
TILE_134D =134
TILE_136D = 136
TILE_138D = 138
TILE_153D = 153
TILE_154D = 154
TILE_170D = 170
TILE_170DD = 170
TILE_170DDD = 170
TILE_171D = 171
TILE_171DD = 171
TILE_171DDD = 171
TILE_172D = 172
TILE_172DD = 172
TILE_172DDD = 172
TILE_181D = 181
TILE_181DD = 181
TILE_181DDD = 181
TILE_183D = 183

# Addendum Tiles

TILE_ADDENDUM_1 = 1001
TILE_ADDENDUM_2 = 1002
TILE_ADDENDUM_3 = 1003
TILE_ADDENDUM_4 = 1004
TILE_ADDENDUM_5 = 1005
TILE_ADDENDUM_6 = 1006
TILE_ADDENDUM_7 = 1007
TILE_ADDENDUM_8 = 1008
TILE_ADDENDUM_9 = 1009

# ALL CONNECTORS

TILE_ALL_1LL =1010
TILE_ALL_1MM =1010
TILE_ALL_1TT =1010
TILE_ALL_1LM =1010
TILE_ALL_1LT =1010
TILE_ALL_1ML =1010
TILE_ALL_1MT =1010
TILE_ALL_1TL =1010
TILE_ALL_1TM =1010

TILE_ALL_2LL =1020
TILE_ALL_2MM =1020
TILE_ALL_2TT =1020
TILE_ALL_2LM =1020
TILE_ALL_2LT =1020
TILE_ALL_2ML =1020
TILE_ALL_2MT =1020
TILE_ALL_2TL =1020
TILE_ALL_2TM =1020

TILE_ALL_3LL =1030
TILE_ALL_3MM =1030
TILE_ALL_3TT =1030
TILE_ALL_3LM =1030
TILE_ALL_3LT =1030
TILE_ALL_3ML =1030
TILE_ALL_3MT =1030
TILE_ALL_3TL =1030
TILE_ALL_3TM =1030



"""Tile Rules (also called "adjecency" rules)

There sets of rules represent the way in which the tiles are allowed
to be put together, a.k.a which tile is allowed to be next to which tile.
"""
tileRules = {
    TILE_001 : [LOW, LOW],
    TILE_002 : [LOW, LOW],
    TILE_003 : [LOW, MID],
    TILE_004 : [TOP, TOP],
    TILE_005 : [LOW, LOW],
    TILE_005D : [LOW, MID], # Duplicate of prev. tile
    TILE_006 : [LOW, MID],
    TILE_007 : [MID, MID],
    TILE_008 : [MID, LOW],
    TILE_009 : [LOW, MID],
    TILE_010 : [MID, MID],
    TILE_011 : [LOW, LOW],
    TILE_012 : [LOW, LOW], 
    TILE_013 : [LOW, LOW],
    TILE_014 : [LOW, MID],
    TILE_015 : [LOW, LOW],
    TILE_015D : [MID, LOW], # Duplicate of prev. tile
    TILE_016 : [LOW, LOW],
    TILE_017 : [LOW, LOW],
    TILE_017D : [MID, MID], # Duplicate of prev. tile
    TILE_018 : [LOW, LOW],
    TILE_019 : [LOW, LOW],
    TILE_019D : [LOW, MID], # Duplicate of prev. tile
    TILE_020 : [LOW, LOW],
    TILE_020D : [MID, LOW], # Duplicate of prev. tile
    TILE_021 : [LOW, LOW],
    TILE_022 : [LOW, MID],
    TILE_023 : [LOW, LOW],
    TILE_024 : [LOW, LOW],
    TILE_025 : [LOW, LOW],
    TILE_025D : [LOW, MID], # Duplicate of prev. tile
    TILE_026 : [LOW, LOW],
    TILE_026D : [MID, LOW], # Duplicate of prev. tile
    TILE_027 : [LOW, TOP],
    TILE_028 : [LOW, LOW],
    TILE_029 : [LOW, LOW],
    TILE_030 : [LOW, LOW],
    TILE_031 : [LOW, LOW],
    TILE_032 : [LOW, LOW],
    TILE_033 : [LOW, LOW],
    TILE_034 : [LOW, LOW],
    TILE_035 : [LOW, LOW],
    TILE_036 : [LOW, LOW],
    TILE_037 : [LOW, LOW],
    TILE_038 : [LOW, MID],
    TILE_039 : [LOW, LOW],
    TILE_040 : [LOW, LOW],
    TILE_040D : [LOW, MID], # Duplicate of prev. tile
    TILE_041 : [LOW, LOW],
    TILE_042 : [LOW, LOW],
    TILE_043 : [LOW, LOW],
    TILE_044 : [LOW, LOW],
    TILE_045 : [LOW, LOW],
    TILE_046 : [LOW, LOW],
    TILE_046D : [MID, MID], # Duplicate of prev. tile
    TILE_047 : [LOW, LOW],
    TILE_048 : [LOW, LOW],
    TILE_049 : [LOW, LOW],
    TILE_049D : [MID, MID], # Duplicate of prev. tile
    TILE_050 : [LOW, LOW],
    TILE_051 : [LOW, LOW],
    TILE_052 : [LOW, MID],
    TILE_053 : [LOW, MID],
    TILE_054 : [LOW, MID],
    TILE_054D : [TOP, MID], # Duplicate of prev. tile
    TILE_055 : [MID, LOW],
    TILE_055D : [LOW, LOW], # Duplicate of prev. tile
    TILE_056 : [LOW, LOW],
    TILE_056D : [MID, MID], # Duplicate of prev. tile
    TILE_057 : [LOW, LOW],
    TILE_057D : [LOW, TOP], # Duplicate of prev. tile
    TILE_058 : [MID, MID],
    TILE_059 : [LOW, MID],
    TILE_060 : [LOW, LOW],
    TILE_060D : [MID, LOW], # Duplicate of prev. tile
    TILE_061 : [LOW, LOW],
    TILE_062 : [MID, LOW],
    TILE_063 : [LOW, LOW],
    TILE_064 : [LOW, LOW],
    TILE_065 : [LOW, LOW],
    TILE_066 : [LOW, LOW],
    TILE_067 : [LOW, LOW],
    TILE_068 : [LOW, LOW],
    TILE_069 : [LOW, MID],
    TILE_070 : [LOW, LOW],
    TILE_071 : [LOW, LOW],
    TILE_071D : [LOW, MID], # Duplicate of prev. tile
    TILE_072 : [TOP, LOW],
    TILE_072D : [LOW, LOW], # Duplicate of prev. tile
    TILE_073 : [MID, LOW],
    TILE_074 : [TOP, TOP],
    TILE_074D : [TOP, MID], # Duplicate of prev. tile
    TILE_074DD : [TOP, LOW], # Duplicate of 74
    TILE_075 : [MID, MID],
    TILE_076 : [TOP, MID],
    TILE_076D : [MID, MID], # Duplicate of prev. tile
    TILE_076DD : [MID, LOW], # Duplicate of 76
    TILE_077 : [TOP, MID],
    TILE_078 : [LOW, LOW],
    TILE_079 : [LOW, TOP],
    TILE_080 : [LOW, LOW],
    TILE_081 : [LOW, LOW],
    TILE_082 : [LOW, LOW],
    TILE_083 : [LOW, LOW],
    TILE_084 : [LOW, LOW],
    TILE_085 : [LOW, LOW],
    TILE_086 : [LOW, LOW],
    TILE_087 : [LOW, LOW],
    TILE_088 : [LOW, LOW],
    TILE_089 : [LOW, MID],
    TILE_089D : [LOW, LOW], # Duplicate of prev. tile
    TILE_090 : [LOW, LOW],
    TILE_091 : [LOW, MID],
    TILE_091D : [LOW, LOW], # Duplicate of prev. tile
    TILE_092 : [LOW, LOW],
    TILE_093 : [LOW, MID],
    TILE_094 : [LOW, MID],
    TILE_094D : [LOW, LOW], # Duplicate of prev. tile
    TILE_095 : [MID, LOW],
    TILE_095D : [LOW, LOW], # Duplicate of prev. tile
    TILE_096 : [LOW, MID],
    TILE_096D : [LOW, LOW], # Duplicate of prev. tile
    TILE_097 : [LOW, LOW],
    TILE_098 : [LOW, LOW],
    TILE_099 : [LOW, LOW],
    TILE_100 : [LOW, LOW],
    TILE_101 : [LOW, MID],
    TILE_102 : [LOW, LOW],
    TILE_103 : [LOW, LOW],
    TILE_103D : [LOW, MID], # Duplicate of prev. tile
    TILE_104 : [LOW, LOW],
    TILE_105 : [LOW, LOW],
    TILE_106 : [MID, LOW],
    TILE_107 : [LOW, LOW],
    TILE_108 : [LOW, LOW],
    TILE_109 : [LOW, MID],
    TILE_110 : [MID, LOW],
    TILE_110D : [LOW, LOW], # Duplicate of prev. tile
    TILE_111 : [LOW, LOW],
    TILE_112 : [LOW, LOW],
    TILE_113 : [LOW, LOW],
    TILE_114 : [MID, MID],
    TILE_114D : [LOW, LOW], # Duplicate of prev. tile
    TILE_115 : [MID, MID],
    TILE_115D : [LOW, MID], # Duplicate of prev. tile
    TILE_116 : [LOW, LOW],
    TILE_117 : [LOW, MID],
    TILE_117D : [LOW, LOW], # Duplicate of prev. tile
    TILE_118 : [MID, MID],
    TILE_118D : [LOW, LOW], # Duplicate of prev. tile
    TILE_119 : [LOW, LOW],
    TILE_120 : [MID, MID],
    TILE_120D : [MID, LOW], # Duplicate of prev. tile
    TILE_120DD : [LOW, MID], # Duplicate of 120
    TILE_120DDD : [LOW, LOW], # Duplicate of 120
    TILE_121 : [LOW, LOW],
    TILE_122 : [LOW, MID],
    TILE_123 : [LOW, LOW],
    TILE_124 : [LOW, LOW],
    TILE_125 : [MID, LOW],
    TILE_125D : [LOW, LOW], # Duplicate of prev. tile
    TILE_126 : [MID, LOW],
    TILE_127 : [LOW, LOW],
    TILE_128 : [MID, MID],
    TILE_128D : [LOW, MID], # Duplicate of prev. tile
    TILE_129 : [MID, MID],
    TILE_130 : [MID, LOW],
    TILE_131 : [LOW, MID],
    TILE_131D : [LOW, LOW], # Duplicate of prev. tile
    TILE_132 : [LOW, LOW],
    TILE_133 : [LOW, LOW],
    TILE_134 : [LOW, MID],
    TILE_134D : [LOW, LOW], # Duplicate of prev. tile
    TILE_135 : [LOW, LOW],
    TILE_136 : [LOW, MID],
    TILE_136D : [LOW, LOW], # Duplicate of prev. tile
    TILE_137 : [LOW, LOW],
    TILE_138 : [LOW, MID],
    TILE_138D : [LOW, LOW], # Duplicate of prev. tile
    TILE_139 : [LOW, MID],
    TILE_140 : [LOW, LOW],
    TILE_141 : [LOW, LOW],
    TILE_142 : [LOW, LOW],
    TILE_143 : [LOW, LOW],
    TILE_144 : [LOW, LOW],
    TILE_145 : [LOW, LOW],
    TILE_146 : [LOW, LOW],
    TILE_147 : [LOW, LOW],
    TILE_148 : [LOW, LOW],
    TILE_149 : [LOW, LOW],
    TILE_150 : [LOW, LOW],
    TILE_151 : [LOW, LOW],
    TILE_152 : [LOW, LOW],
    TILE_153 : [LOW, MID],
    TILE_153D : [LOW, LOW], # Duplicate of prev. tile
    TILE_154 : [MID, LOW],
    TILE_154D : [LOW, LOW], # Duplicate of prev. tile
    TILE_155 : [LOW, LOW],
    TILE_156 : [LOW, LOW],
    TILE_157 : [LOW, LOW],
    TILE_158 : [LOW, LOW],
    TILE_159 : [LOW, MID],
    TILE_160 : [LOW, LOW],
    TILE_161 : [LOW, LOW],
    TILE_162 : [LOW, LOW],
    TILE_163 : [LOW, LOW],
    TILE_164 : [LOW, LOW],
    TILE_165 : [LOW, LOW],
    TILE_166 : [LOW, MID],
    TILE_167 : [LOW, MID],
    TILE_168 : [LOW, MID],
    TILE_169 : [LOW, LOW],
    TILE_170 : [MID, MID],
    TILE_170D : [MID, LOW], # Duplicate of prev. tile
    TILE_170DD : [LOW, MID], # Duplicate of 170
    TILE_170DDD : [LOW, LOW], # Duplicate of 170
    TILE_171 : [MID, MID],
    TILE_171D : [MID, LOW], # Duplicate of prev. tile
    TILE_171DD : [LOW, MID], # Duplicate of 171
    TILE_171DDD : [LOW, LOW], # Duplicate of 171
    TILE_172 : [MID, MID],
    TILE_172D : [MID, LOW], # Duplicate of prev. tile
    TILE_172DD : [LOW, MID], # Duplicate of 172
    TILE_172DDD : [LOW, LOW], # Duplicate of 172
    TILE_173 : [LOW, LOW],
    TILE_174 : [LOW, LOW],
    TILE_175 : [LOW, LOW],
    TILE_176 : [LOW, LOW],
    TILE_177 : [LOW, LOW],
    TILE_178 : [LOW, LOW],
    TILE_179 : [LOW, LOW],
    TILE_180 : [LOW, MID],
    TILE_181 : [MID, MID],
    TILE_181D : [MID, LOW], # Duplicate of prev. tile
    TILE_181DD : [LOW, MID], # Duplicate of 181
    TILE_181DDD : [LOW, LOW], # Duplicate of 181
    TILE_182 : [LOW, LOW],
    TILE_183 : [MID, LOW],
    TILE_183D : [LOW, LOW], # Duplicate of prev. tile
    TILE_184 : [LOW, LOW],
    TILE_185 : [LOW, MID],
    
    # Addendum Tiles:

    TILE_ADDENDUM_1 : [TOP, TOP],
    TILE_ADDENDUM_2 : [TOP, TOP],
    TILE_ADDENDUM_3 : [LOW, TOP],
    TILE_ADDENDUM_4 : [MID, LOW],
    TILE_ADDENDUM_5 : [MID, TOP],
    TILE_ADDENDUM_6 : [MID, TOP],
    TILE_ADDENDUM_7 : [MID, TOP],
    TILE_ADDENDUM_8 : [TOP, LOW],
    TILE_ADDENDUM_9 : [TOP, MID],

    # ALL CONNECTORS

    TILE_ALL_1LL : [LOW,LOW],
    TILE_ALL_1MM : [MID,MID],
    TILE_ALL_1TT : [TOP,TOP],
    TILE_ALL_1LM : [LOW,MID],
    TILE_ALL_1LT : [LOW,TOP],
    TILE_ALL_1ML : [MID,LOW],
    TILE_ALL_1MT : [MID,TOP],
    TILE_ALL_1TL : [TOP,LOW],
    TILE_ALL_1TM : [TOP,MID],

    TILE_ALL_2LL : [LOW,LOW],
    TILE_ALL_2MM : [MID,MID],
    TILE_ALL_2TT : [TOP,TOP],
    TILE_ALL_2LM : [LOW,MID],
    TILE_ALL_2LT : [LOW,TOP],
    TILE_ALL_2ML : [MID,LOW],
    TILE_ALL_2MT : [MID,TOP],
    TILE_ALL_2TL : [TOP,LOW],
    TILE_ALL_2TM : [TOP,MID],

    TILE_ALL_3LL : [LOW,LOW],
    TILE_ALL_3MM : [MID,MID],
    TILE_ALL_3TT : [TOP,TOP],
    TILE_ALL_3LM : [LOW,MID],
    TILE_ALL_3LT : [LOW,TOP],
    TILE_ALL_3ML : [MID,LOW],
    TILE_ALL_3MT : [MID,TOP],
    TILE_ALL_3TL : [TOP,LOW],
    TILE_ALL_3TM : [TOP,MID],

}


"""Tile Difficulty

Difficulty values aassociated with each tile.
"""
tileDifficulty = {
    TILE_001: [EASY],
    TILE_002: [MEDIUM],
    TILE_003: [EASY],
    TILE_004: [MEDIUM],
    TILE_005: [EASY],
    TILE_005D: [EASY],
    TILE_006: [MEDIUM],
    TILE_007: [HARD],
    TILE_008: [HARD],
    TILE_009: [MEDIUM],
    TILE_010: [EASY],
    TILE_011: [MEDIUM],
    TILE_012: [EASY],
    TILE_013: [EASY],
    TILE_014: [EASY],
    TILE_015: [MEDIUM],
    TILE_015D: [MEDIUM],
    TILE_016: [MEDIUM],
    TILE_017: [MEDIUM],
    TILE_017D: [MEDIUM],
    TILE_018: [HARD],
    TILE_019: [EASY],
    TILE_019D: [EASY],
    TILE_020: [MEDIUM],
    TILE_020D: [MEDIUM],
    TILE_021: [MEDIUM],
    TILE_022: [MEDIUM],
    TILE_023: [MEDIUM],
    TILE_024: [MEDIUM],
    TILE_025: [MEDIUM],
    TILE_025D: [MEDIUM],
    TILE_026: [MEDIUM],
    TILE_026D: [MEDIUM],
    TILE_027: [EASY],
    TILE_028: [EASY],
    TILE_029: [EASY],
    TILE_030: [EASY],
    TILE_031: [EASY],
    TILE_032: [MEDIUM],
    TILE_033: [MEDIUM],
    TILE_034: [MEDIUM],
    TILE_035: [MEDIUM],
    TILE_036: [EASY],
    TILE_037: [MEDIUM],
    TILE_038: [EASY],
    TILE_039: [MEDIUM],
    TILE_040: [EASY],
    TILE_040D: [EASY],
    TILE_041: [MEDIUM],
    TILE_042: [MEDIUM],
    TILE_043: [HARD],
    TILE_044: [MEDIUM],
    TILE_045: [HARD],
    TILE_046: [MEDIUM],
    TILE_046D: [MEDIUM],
    TILE_047: [MEDIUM],
    TILE_048: [MEDIUM],
    TILE_049: [HARD],
    TILE_049D: [HARD],
    TILE_050: [MEDIUM],
    TILE_051: [MEDIUM],
    TILE_052: [MEDIUM],
    TILE_053: [MEDIUM],
    TILE_054: [MEDIUM],
    TILE_054D: [MEDIUM],
    TILE_055: [MEDIUM],
    TILE_055D: [MEDIUM],
    TILE_056: [EASY],
    TILE_056D: [EASY],
    TILE_057: [MEDIUM],
    TILE_057D: [MEDIUM],
    TILE_058: [HARD],
    TILE_059: [HARD],
    TILE_060: [MEDIUM],
    TILE_060D: [MEDIUM],
    TILE_061: [MEDIUM],
    TILE_062: [MEDIUM],
    TILE_063: [MEDIUM],
    TILE_064: [EASY],
    TILE_065: [MEDIUM],
    TILE_066: [MEDIUM],
    TILE_067: [MEDIUM],
    TILE_068: [HARD],
    TILE_069: [MEDIUM],
    TILE_070: [EASY],
    TILE_071: [EASY],
    TILE_071D: [EASY],
    TILE_072: [EASY],
    TILE_072D: [EASY],
    TILE_073: [MEDIUM],
    TILE_074: [MEDIUM],
    TILE_074D: [MEDIUM],
    TILE_074DD: [MEDIUM],
    TILE_075: [HARD],
    TILE_076: [HARD],
    TILE_076D: [HARD],
    TILE_076DD: [HARD],
    TILE_077: [MEDIUM],
    TILE_078: [MEDIUM],
    TILE_079: [MEDIUM],
    TILE_080: [HARD],
    TILE_081: [MEDIUM],
    TILE_082: [MEDIUM],
    TILE_083: [HARD],
    TILE_084: [MEDIUM],
    TILE_085: [HARD],
    TILE_086: [MEDIUM],
    TILE_087: [MEDIUM],
    TILE_088: [MEDIUM],
    TILE_089: [EASY],
    TILE_089D: [EASY],
    TILE_090: [EASY],
    TILE_091: [MEDIUM],
    TILE_091D: [MEDIUM],
    TILE_092: [MEDIUM],
    TILE_093: [MEDIUM],
    TILE_094: [MEDIUM],
    TILE_094D: [MEDIUM],
    TILE_095: [MEDIUM],
    TILE_095D: [MEDIUM],
    TILE_096: [MEDIUM],
    TILE_096D: [MEDIUM],
    TILE_097: [MEDIUM],
    TILE_098: [MEDIUM],
    TILE_099: [MEDIUM],
    TILE_100: [MEDIUM],
    TILE_101: [MEDIUM],
    TILE_102: [MEDIUM],
    TILE_103: [EASY],
    TILE_103D: [EASY],
    TILE_104: [MEDIUM],
    TILE_105: [MEDIUM],
    TILE_106: [MEDIUM],
    TILE_107: [MEDIUM],
    TILE_108: [EASY],
    TILE_109: [MEDIUM],
    TILE_110: [MEDIUM],
    TILE_110D: [MEDIUM],
    TILE_111: [MEDIUM],
    TILE_112: [MEDIUM],
    TILE_113: [MEDIUM],
    TILE_114: [MEDIUM],
    TILE_114D: [MEDIUM],
    TILE_115: [MEDIUM],
    TILE_115D: [MEDIUM],
    TILE_116: [MEDIUM],
    TILE_117: [MEDIUM],
    TILE_117D: [MEDIUM],
    TILE_118: [MEDIUM],
    TILE_118D: [MEDIUM],
    TILE_119: [MEDIUM],
    TILE_120: [MEDIUM],
    TILE_120D: [MEDIUM],
    TILE_120DD: [MEDIUM],
    TILE_120DDD: [MEDIUM],
    TILE_121: [MEDIUM],
    TILE_122: [MEDIUM],
    TILE_123: [EASY],
    TILE_124: [MEDIUM],
    TILE_125: [MEDIUM],
    TILE_125D: [MEDIUM],
    TILE_126: [MEDIUM],
    TILE_127: [MEDIUM],
    TILE_128: [MEDIUM],
    TILE_128D: [MEDIUM],
    TILE_129: [HARD],
    TILE_130: [MEDIUM],
    TILE_131: [HARD],
    TILE_131D: [HARD],
    TILE_132: [MEDIUM],
    TILE_133: [MEDIUM],
    TILE_134D: [HARD],
    TILE_135: [MEDIUM],
    TILE_136D: [MEDIUM],
    TILE_137: [MEDIUM],
    TILE_138: [MEDIUM],
    TILE_138D: [MEDIUM],
    TILE_139: [EASY],
    TILE_140: [MEDIUM],
    TILE_141: [MEDIUM],
    TILE_142: [MEDIUM],
    TILE_143: [HARD],
    TILE_144: [HARD],
    TILE_145: [MEDIUM],
    TILE_146: [EASY],
    TILE_147: [HARD],
    TILE_148: [HARD],
    TILE_149: [MEDIUM],
    TILE_150: [MEDIUM],
    TILE_151: [HARD],
    TILE_152: [HARD],
    TILE_153: [MEDIUM],
    TILE_153D: [MEDIUM],
    TILE_154: [MEDIUM],
    TILE_154D: [MEDIUM],
    TILE_155: [HARD],
    TILE_156: [HARD],
    TILE_157: [MEDIUM],
    TILE_158: [MEDIUM],
    TILE_159: [HARD],
    TILE_160: [HARD],
    TILE_161: [MEDIUM],
    TILE_162: [MEDIUM],
    TILE_163: [EASY],
    TILE_164: [EASY],
    TILE_165: [MEDIUM],
    TILE_166: [MEDIUM],
    TILE_167: [HARD],
    TILE_168: [HARD],
    TILE_169: [EASY],
    TILE_170: [MEDIUM],
    TILE_170D: [MEDIUM],
    TILE_170DD: [MEDIUM],
    TILE_170DDD: [MEDIUM],
    TILE_171: [MEDIUM],
    TILE_171D: [MEDIUM],
    TILE_171DD: [MEDIUM],
    TILE_171DDD: [MEDIUM],
    TILE_172: [MEDIUM],
    TILE_172D: [MEDIUM],
    TILE_172DD: [MEDIUM],
    TILE_172DDD: [MEDIUM],
    TILE_173: [MEDIUM],
    TILE_174: [HARD],
    TILE_175: [HARD],
    TILE_176: [MEDIUM],
    TILE_177: [MEDIUM],
    TILE_178: [HARD],
    TILE_179: [HARD],
    TILE_180: [MEDIUM],
    TILE_181: [MEDIUM],
    TILE_181D: [MEDIUM],
    TILE_181DD: [MEDIUM],
    TILE_181DDD: [MEDIUM],
    TILE_182: [MEDIUM],
    TILE_183: [MEDIUM],
    TILE_183D: [MEDIUM],
    TILE_184: [MEDIUM],
    TILE_185: [HARD],

    # Addendum Tiles

    TILE_ADDENDUM_1 : [EASY],
    TILE_ADDENDUM_2 : [HARD],
    TILE_ADDENDUM_3 : [HARD],
    TILE_ADDENDUM_4 : [EASY],
    TILE_ADDENDUM_5 : [EASY],
    TILE_ADDENDUM_6 : [MEDIUM],
    TILE_ADDENDUM_7 : [HARD],
    TILE_ADDENDUM_8 : [HARD],
    TILE_ADDENDUM_9 : [EASY],

    # ALL CONNECTORS

    TILE_ALL_1LL : [EASY],
    TILE_ALL_1MM : [EASY],
    TILE_ALL_1TT : [EASY],
    TILE_ALL_1LM : [EASY],
    TILE_ALL_1LT : [EASY],
    TILE_ALL_1ML : [EASY],
    TILE_ALL_1MT : [EASY],
    TILE_ALL_1TL : [EASY],
    TILE_ALL_1TM : [EASY],

    TILE_ALL_2LL : [MEDIUM],
    TILE_ALL_2MM : [MEDIUM],
    TILE_ALL_2TT : [MEDIUM],
    TILE_ALL_2LM : [MEDIUM],
    TILE_ALL_2LT : [MEDIUM],
    TILE_ALL_2ML : [MEDIUM],
    TILE_ALL_2MT : [MEDIUM],
    TILE_ALL_2TL : [MEDIUM],
    TILE_ALL_2TM : [MEDIUM],

    TILE_ALL_3LL : [HARD],
    TILE_ALL_3MM : [HARD],
    TILE_ALL_3TT : [HARD],
    TILE_ALL_3LM : [HARD],
    TILE_ALL_3LT : [HARD],
    TILE_ALL_3ML : [HARD],
    TILE_ALL_3MT : [HARD],
    TILE_ALL_3TL : [HARD],
    TILE_ALL_3TM : [HARD],


}

"""Tile Weights

These can be used if `WEIGHTED` variable is set to true and will cause 
the tile choice to be skewed towards tiles with a higher value whenever possible.
"""
tileWeights = {
    TILE_001 : 5,
    TILE_002 : 5,
    TILE_003 : 5,
    TILE_004 : 5,
    TILE_005 : 5,
    TILE_006 : 5,
    TILE_007 : 5,
    TILE_008 : 5,
    TILE_009 : 5,
    TILE_010 : 5,
    TILE_011 : 5,
    TILE_012 : 10,
    TILE_013 : 10,
    TILE_014 : 10,
    TILE_015 : 10,
    TILE_016 : 10,
    TILE_017 : 10,
    TILE_018 : 10,
    TILE_019 : 10,
    TILE_020 : 10,
    TILE_021 : 10,
    TILE_022 : 10,
    TILE_023 : 10,
    TILE_024 : 10,
    TILE_025 : 10,
    TILE_026 : 10,
    TILE_027 : 10,
    TILE_028 : 10,
    TILE_029 : 10,
    TILE_030 : 10,
    TILE_031 : 10,
    TILE_032 : 10,
    TILE_033 : 10,
    TILE_034 : 10,
    TILE_035 : 10,
    TILE_036 : 10,
    TILE_037 : 10,
    TILE_038 : 10,
    TILE_039 : 10,
    TILE_040 : 5,
    TILE_041 : 5,
    TILE_042 : 5,
    TILE_043 : 5,
    TILE_044 : 5,
    TILE_045 : 5,
    TILE_046 : 5,
    TILE_047 : 5,
    TILE_048 : 5,
    TILE_049 : 5,
    TILE_050 : 5,
    TILE_051 : 5,
    TILE_052 : 5,
    TILE_053 : 5,
    TILE_054 : 5,
    TILE_055 : 5,
    TILE_056 : 5,
    TILE_057 : 5,
    TILE_058 : 5,
    TILE_059 : 5,
    TILE_060 : 5,
    TILE_061 : 5,
    TILE_062 : 5,
    TILE_063 : 10,
    TILE_064 : 10,
    TILE_065 : 10,
    TILE_066 : 10,
    TILE_067 : 10,
    TILE_068 : 10,
    TILE_069 : 10,
    TILE_070 : 5,
    TILE_071 : 5,
    TILE_072 : 5,
    TILE_073 : 5,
    TILE_074 : 5,
    TILE_075 : 5,
    TILE_076 : 5,
    TILE_077 : 5,
    TILE_078 : 5,
    TILE_079 : 5,
    TILE_080 : 10,
    TILE_081 : 10,
    TILE_082 : 10,
    TILE_083 : 10,
    TILE_084 : 10,
    TILE_085 : 10,
    TILE_086 : 10,
    TILE_087 : 10,
    TILE_088 : 10,
    TILE_089 : 10,
    TILE_090 : 10,
    TILE_091 : 10,
    TILE_092 : 10,
    TILE_093 : 10,
    TILE_094 : 10,
    TILE_095 : 10,
    TILE_096 : 10,
    TILE_097 : 10,
    TILE_098 : 10,
    TILE_099 : 10,
    TILE_100 : 10,
    TILE_101 : 10,
    TILE_102 : 10,
    TILE_103 : 5,
    TILE_104 : 5,
    TILE_105 : 5,
    TILE_106 : 5,
    TILE_107 : 5,
    TILE_108 : 5,
    TILE_109 : 5,
    TILE_110 : 10,
    TILE_111 : 10,
    TILE_112 : 10,
    TILE_113 : 10,
    TILE_114 : 10,
    TILE_115 : 10,
    TILE_116 : 10,
    TILE_117 : 10,
    TILE_118 : 10,
    TILE_119 : 10,
    TILE_120 : 10,
    TILE_121 : 10,
    TILE_122 : 10,
    TILE_123 : 10,
    TILE_124 : 5,
    TILE_125 : 5,
    TILE_126 : 5,
    TILE_127 : 5,
    TILE_128 : 5,
    TILE_129 : 5,
    TILE_130 : 5,
    TILE_131 : 10,
    TILE_132 : 10,
    TILE_133 : 10,
    TILE_134 : 10,
    TILE_135 : 10,
    TILE_136 : 10,
    TILE_137 : 10,
    TILE_138 : 10,
    TILE_139 : 10,
    TILE_140 : 10,
    TILE_141 : 10,
    TILE_142 : 10,
    TILE_143 : 10,
    TILE_144 : 10,
    TILE_145 : 10,
    TILE_146 : 10,
    TILE_147 : 10,
    TILE_148 : 10,
    TILE_149 : 10,
    TILE_150 : 10,
    TILE_151 : 10,
    TILE_152 : 10,
    TILE_153 : 10,
    TILE_154 : 10,
    TILE_155 : 10,
    TILE_156 : 10,
    TILE_157 : 10,
    TILE_158 : 10,
    TILE_159 : 10,
    TILE_160 : 10,
    TILE_161 : 10,
    TILE_162 : 10,
    TILE_163 : 10,
    TILE_164 : 10,
    TILE_165 : 10,
    TILE_166 : 10,
    TILE_167 : 10,
    TILE_168 : 10,
    TILE_169 : 10,
    TILE_170 : 10,
    TILE_171 : 10,
    TILE_172 : 10,
    TILE_173 : 10,
    TILE_174 : 10,
    TILE_175 : 10,
    TILE_176 : 10,
    TILE_177 : 10,
    TILE_178 : 10,
    TILE_179 : 10,
    TILE_180 : 10,
    TILE_181 : 5,
    TILE_182 : 10,
    TILE_183 : 10,
    TILE_184 : 10,
    TILE_185 : 10,

    # Duplicates:
    TILE_005D : 5,
    TILE_015D : 5,
    TILE_017D : 5, 
    TILE_019D : 5,
    TILE_020D : 5,
    TILE_025D : 5,
    TILE_026D : 5,
    TILE_040D : 5,
    TILE_046D : 5,
    TILE_049D : 5,
    TILE_054D : 5,
    TILE_055D : 5,
    TILE_056D : 5,
    TILE_057D : 5, 
    TILE_060D : 5,
    TILE_071D : 5,
    TILE_072D : 5,
    TILE_074D : 5,
    TILE_074DD : 5,
    TILE_076D : 5,
    TILE_076DD : 5,
    TILE_089D : 5,
    TILE_091D : 5,
    TILE_094D : 5,
    TILE_095D : 5,
    TILE_096D : 5,
    TILE_103D : 5,
    TILE_110D : 5,
    TILE_114D : 5,
    TILE_115D : 5,
    TILE_117D : 5,
    TILE_118D : 5,
    TILE_120D : 5,
    TILE_120DD : 5,
    TILE_120DDD : 5,
    TILE_125D : 5,
    TILE_128D : 5,
    TILE_131D : 5,
    TILE_134D : 5,
    TILE_136D : 5,
    TILE_138D : 5,
    TILE_153D : 5,
    TILE_154D : 5,
    TILE_170D : 5,
    TILE_170DD : 5,
    TILE_170DDD : 5,
    TILE_171D : 5,
    TILE_171DD : 5,
    TILE_171DDD : 5,
    TILE_172D : 5,
    TILE_172DD : 5, 
    TILE_172DDD : 5,
    TILE_181D : 5,
    TILE_181DD : 5,
    TILE_181DDD : 5,
    TILE_183D : 5,

    # Addendum Tiles

    TILE_ADDENDUM_1 : 2,
    TILE_ADDENDUM_2 : 2,
    TILE_ADDENDUM_3 : 2,
    TILE_ADDENDUM_4 : 2,
    TILE_ADDENDUM_5 : 2,
    TILE_ADDENDUM_6 : 2,
    TILE_ADDENDUM_7 : 2,
    TILE_ADDENDUM_8 : 2,
    TILE_ADDENDUM_9 : 2,

    # ALL CONNECTORS

    TILE_ALL_1LL : 1,
    TILE_ALL_1MM : 1,
    TILE_ALL_1TT : 1,
    TILE_ALL_1LM : 1,
    TILE_ALL_1LT : 1,
    TILE_ALL_1ML : 1,
    TILE_ALL_1MT : 1,
    TILE_ALL_1TL : 1,
    TILE_ALL_1TM : 1,

    TILE_ALL_2LL : 1,
    TILE_ALL_2MM : 1,
    TILE_ALL_2TT : 1,
    TILE_ALL_2LM : 1,
    TILE_ALL_2LT : 1,
    TILE_ALL_2ML : 1,
    TILE_ALL_2MT : 1,
    TILE_ALL_2TL : 1,
    TILE_ALL_2TM : 1,

    TILE_ALL_3LL : 1,
    TILE_ALL_3MM : 1,
    TILE_ALL_3TT : 1,
    TILE_ALL_3LM : 1,
    TILE_ALL_3LT : 1,
    TILE_ALL_3ML : 1,
    TILE_ALL_3MT : 1,
    TILE_ALL_3TL : 1,
    TILE_ALL_3TM : 1,
}


"""Tile Sprites

Location in the image file (refered in `SPRITE_PATH` variable) 
where each tile starts.
"""
tileSprites = {
    TILE_001 : (0, 0),
    TILE_002 : (160, 0),
    TILE_003 : (320, 0),
    TILE_004 : (480, 0),
    TILE_005 : (640, 0),
    TILE_006 : (800, 0),
    TILE_007 : (960, 0),
    TILE_008 : (1120, 0),
    TILE_009 : (1280, 0),
    TILE_010 : (1440, 0),
    TILE_011 : (1600, 0),
    TILE_012 : (1760, 0),
    TILE_013 : (1920, 0),
    TILE_014 : (2080, 0),
    TILE_015 : (2240, 0),
    TILE_016 : (2400, 0),
    TILE_017 : (2560, 0),
    TILE_018 : (2720, 0),
    TILE_019 : (2880, 0),
    TILE_020 : (3040, 0),
    TILE_021 : (3200, 0),
    TILE_022 : (3360, 0),
    TILE_023 : (3520, 0),
    TILE_024 : (3680, 0),
    TILE_025 : (3840, 0),
    TILE_026 : (4000, 0),
    TILE_027 : (4160, 0),
    TILE_028 : (4320, 0),
    TILE_029 : (4480, 0),
    TILE_030 : (4640, 0),
    TILE_031 : (4800, 0),
    TILE_032 : (4960, 0),
    TILE_033 : (5120, 0),
    TILE_034 : (5280, 0),
    TILE_035 : (5440, 0),
    TILE_036 : (5600, 0),
    TILE_037 : (5760, 0),
    TILE_038 : (5920, 0),
    TILE_039 : (6080, 0),
    TILE_040 : (6240, 0),
    TILE_041 : (6400, 0),
    TILE_042 : (6560, 0),
    TILE_043 : (6720, 0),
    TILE_044 : (6880, 0),
    TILE_045 : (7040, 0),
    TILE_046 : (7200, 0),
    TILE_047 : (7360, 0),
    TILE_048 : (7520, 0),
    TILE_049 : (7680, 0),
    TILE_050 : (7840, 0),
    TILE_051 : (8000, 0),
    TILE_052 : (8160, 0),
    TILE_053 : (8320, 0),
    TILE_054 : (8480, 0),
    TILE_055 : (8640, 0),
    TILE_056 : (8800, 0),
    TILE_057 : (8960, 0),
    TILE_058 : (9120, 0),
    TILE_059 : (9280, 0),
    TILE_060 : (9440, 0),
    TILE_061 : (9600, 0),
    TILE_062 : (9760, 0),
    TILE_063 : (9920, 0),
    TILE_064 : (10080, 0),
    TILE_065 : (10240, 0),
    TILE_066 : (10400, 0),
    TILE_067 : (10560, 0),
    TILE_068 : (10720, 0),
    TILE_069 : (10880, 0),
    TILE_070 : (11040, 0),
    TILE_071 : (11200, 0),
    TILE_072 : (11360, 0),
    TILE_073 : (11520, 0),
    TILE_074 : (11680, 0),
    TILE_075 : (11840, 0),
    TILE_076 : (12000, 0),
    TILE_077 : (12160, 0),
    TILE_078 : (12320, 0),
    TILE_079 : (12480, 0),
    TILE_080 : (12640, 0),
    TILE_081 : (12800, 0),
    TILE_082 : (12960, 0),
    TILE_083 : (13120, 0),
    TILE_084 : (13280, 0),
    TILE_085 : (13440, 0),
    TILE_086 : (13600, 0),
    TILE_087 : (13760, 0),
    TILE_088 : (13920, 0),
    TILE_089 : (14080, 0),
    TILE_090 : (14240, 0),
    TILE_091 : (14400, 0),
    TILE_092 : (14560, 0),
    TILE_093 : (14720, 0),
    TILE_094 : (14880, 0),
    TILE_095 : (15040, 0),
    TILE_096 : (15200, 0),
    TILE_097 : (15360, 0),
    TILE_098 : (15520, 0),
    TILE_099 : (15680, 0),
    TILE_100 : (15840, 0),
    TILE_101 : (16000, 0),
    TILE_102 : (16160, 0),
    TILE_103 : (16320, 0),
    TILE_104 : (16480, 0),
    TILE_105 : (16640, 0),
    TILE_106 : (16800, 0),
    TILE_107 : (16960, 0),
    TILE_108 : (17120, 0),
    TILE_109 : (17280, 0),
    TILE_110 : (17440, 0),
    TILE_111 : (17600, 0),
    TILE_112 : (17760, 0),
    TILE_113 : (17920, 0),
    TILE_114 : (18080, 0),
    TILE_115 : (18240, 0),
    TILE_116 : (18400, 0),
    TILE_117 : (18560, 0),
    TILE_118 : (18720, 0),
    TILE_119 : (18880, 0),
    TILE_120 : (19040, 0),
    TILE_121 : (19200, 0),
    TILE_122 : (19360, 0),
    TILE_123 : (19520, 0),
    TILE_124 : (19680, 0),
    TILE_125 : (19840, 0),
    TILE_126 : (20000, 0),
    TILE_127 : (20160, 0),
    TILE_128 : (20320, 0),
    TILE_129 : (20480, 0),
    TILE_130 : (20640, 0),
    TILE_131 : (20800, 0),
    TILE_132 : (20960, 0),
    TILE_133 : (21120, 0),
    TILE_134 : (21280, 0),
    TILE_135 : (21440, 0),
    TILE_136 : (21600, 0),
    TILE_137 : (21760, 0),
    TILE_138 : (21920, 0),
    TILE_139 : (22080, 0),
    TILE_140 : (22240, 0),
    TILE_141 : (22400, 0),
    TILE_142 : (22560, 0),
    TILE_143 : (22720, 0),
    TILE_144 : (22880, 0),
    TILE_145 : (23040, 0),
    TILE_146 : (23200, 0),
    TILE_147 : (23360, 0),
    TILE_148 : (23520, 0),
    TILE_149 : (23680, 0),
    TILE_150 : (23840, 0),
    TILE_151 : (24000, 0),
    TILE_152 : (24160, 0),
    TILE_153 : (24320, 0),
    TILE_154 : (24480, 0),
    TILE_155 : (24640, 0),
    TILE_156 : (24800, 0),
    TILE_157 : (24960, 0),
    TILE_158 : (25120, 0),
    TILE_159 : (25280, 0),
    TILE_160 : (25440, 0),
    TILE_161 : (25600, 0),
    TILE_162 : (25760, 0),
    TILE_163 : (25920, 0),
    TILE_164 : (26080, 0),
    TILE_165 : (26240, 0),
    TILE_166 : (26400, 0),
    TILE_167 : (26560, 0),
    TILE_168 : (26720, 0),
    TILE_169 : (26880, 0),
    TILE_170 : (27040, 0),
    TILE_171 : (27200, 0),
    TILE_172 : (27360, 0),
    TILE_173 : (27520, 0),
    TILE_174 : (27680, 0),
    TILE_175 : (27840, 0),
    TILE_176 : (28000, 0),
    TILE_177 : (28160, 0),
    TILE_178 : (28320, 0),
    TILE_179 : (28480, 0),
    TILE_180 : (28640, 0),
    TILE_181 : (28800, 0),
    TILE_182 : (28960, 0),
    TILE_183 : (29120, 0),
    TILE_184 : (29280, 0),
    TILE_185 : (29440, 0),


    # Duplicates: 
    TILE_005D : (640, 0), 
    TILE_015D : (2240, 0), 
    TILE_017D : (2560, 0), 
    TILE_019D : (2880, 0), 
    TILE_020D : (3040, 0), 
    TILE_025D : (3840, 0), 
    TILE_026D : (4000, 0), 
    TILE_040D : (6720, 0),
    TILE_046D : (7680, 0), 
    TILE_049D : (8160, 0), 
    TILE_054D : (8480, 0),
    TILE_055D : (8640, 0),
    TILE_056D : (8800, 0),
    TILE_057D : (8960, 0),
    TILE_060D : (9440, 0),
    TILE_071D : (11200, 0),
    TILE_072D : (11360, 0),
    TILE_074D : (11680, 0),
    TILE_074DD : (11680, 0),
    TILE_076D : (12000, 0),
    TILE_076DD : (12000, 0),
    TILE_089D : (14080, 0),
    TILE_091D : (14400, 0),
    TILE_094D : (14880, 0),
    TILE_095D : (15040, 0),
    TILE_096D : (15200, 0),
    TILE_103D : (16320, 0),
    TILE_110D : (17440, 0),
    TILE_114D : (18080, 0),
    TILE_115D : (18240, 0),
    TILE_117D : (18560, 0),
    TILE_118D : (18720, 0),
    TILE_120D : (19040, 0),
    TILE_120DD : (19040, 0),
    TILE_120DDD : (19040, 0),
    TILE_125D : (19840, 0),
    TILE_128D : (20320, 0),
    TILE_131D : (20800, 0),
    TILE_134D : (21280, 0),
    TILE_136D : (21600, 0),
    TILE_138D : (21920, 0),
    TILE_153D : (24320, 0),
    TILE_154D : (24480, 0),
    TILE_170D : (27040, 0),
    TILE_170DD : (27040, 0),
    TILE_170DDD : (27040, 0),
    TILE_171D : (27200, 0),
    TILE_171DD : (27200, 0),
    TILE_171DDD : (27200, 0),
    TILE_172D : (27360, 0),
    TILE_172DD : (27360, 0),
    TILE_172DDD : (27360, 0),
    TILE_181D : (28800, 0),
    TILE_181DD : (28800, 0),
    TILE_181DDD : (28800, 0),
    TILE_183D : (29120, 0),

    # Addendum Tiles

    TILE_ADDENDUM_1 : (29600,0),
    TILE_ADDENDUM_2 : (29760,0),
    TILE_ADDENDUM_3 : (29920,0),
    TILE_ADDENDUM_4 : (30080,0),
    TILE_ADDENDUM_5 : (30240,0),
    TILE_ADDENDUM_6 : (30400,0),
    TILE_ADDENDUM_7 : (30560,0),
    TILE_ADDENDUM_8 : (30720,0),
    TILE_ADDENDUM_9 : (30880,0),

    # ALL CONNECTORS

    TILE_ALL_1LL : (31040,0),
    TILE_ALL_1MM : (31040,0),
    TILE_ALL_1TT : (31040,0),
    TILE_ALL_1LM : (31040,0),
    TILE_ALL_1LT : (31040,0),
    TILE_ALL_1ML : (31040,0),
    TILE_ALL_1MT : (31040,0),
    TILE_ALL_1TL : (31040,0),
    TILE_ALL_1TM : (31040,0),

    TILE_ALL_2LL : (31200,0),
    TILE_ALL_2MM : (31200,0),
    TILE_ALL_2TT : (31200,0),
    TILE_ALL_2LM : (31200,0),
    TILE_ALL_2LT : (31200,0),
    TILE_ALL_2ML : (31200,0),
    TILE_ALL_2MT : (31200,0),
    TILE_ALL_2TL : (31200,0),
    TILE_ALL_2TM : (31200,0),

    TILE_ALL_3LL : (31360,0),
    TILE_ALL_3MM : (31360,0),
    TILE_ALL_3TT : (31360,0),
    TILE_ALL_3LM : (31360,0),
    TILE_ALL_3LT : (31360,0),
    TILE_ALL_3ML : (31360,0),
    TILE_ALL_3MT : (31360,0),
    TILE_ALL_3TL : (31360,0),
    TILE_ALL_3TM : (31360,0),

}
