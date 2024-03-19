#Controls

INTERACTIVE = True
INTERACTIVE_KEYPRESS = True
WEIGHTED = False

ANXIETY_CURVE = True

TILE_METADATA = True

"""Anxiety Curve Value List

This list defines where tiles of a certain difficulty must be placed in the level.
If the level size (LEVEL_LENGTH variable) changes 
the size of this list must be changed as well.
"""

AC = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# AC = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,2]
# AC = [0,0,0,0,0,1,1,1,1,1,2,2,2,2,2]

#Path to spritesheet
# SPRITESHEET_PATH = "images/tiles/SMB_Sprites_w_Background.png" # Sprites including enemies 
# SPRITESHEET_PATH = "images/tiles/SMBSMB_SPrites_NoEnemies_BlackBg.png" # Black BG
SPRITESHEET_PATH = "images/tiles/SMBSMB_SPrites_NoEnemies_PinkBg.png" # Pink BG

#Amount of tiles per level
LEVEL_LENGTH = 10
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

#Tile Types:
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

#Tile Sides:

LOW = 2 # Represents floor height of 2, 3, 4, 5, 6 (starting a min floor, which is 2, and going up by 4 tiles, which is Marios max jump height w/o run-up)
MID = 7 # 7, 8, 9, 10
TOP = 11 # 11, 12, 13, 14

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
    
}

# # Difficulty Types:
EASY = 0 # Tiles that have no way to harm the player
MEDIUM = 1 # Tiles that have total gaps <= 4 tiles wide
HARD = 2 # Tiles that have total gaps >=5 tiles wide

"""Tile difficulty rules"""
tileDifficulty = {

    TILE_001 : [EASY],
    TILE_002 : [EASY],
    TILE_003 : [EASY],
    TILE_004 : [EASY],
    TILE_005 : [EASY],
    TILE_005D : [EASY], # Duplicate of prev. tile
    TILE_006 : [EASY],
    TILE_007 : [EASY],
    TILE_008 : [EASY],
    TILE_009 : [EASY],
    TILE_010 : [EASY],
    TILE_011 : [EASY],
    TILE_012 : [EASY], 
    TILE_013 : [EASY],
    TILE_014 : [EASY],
    TILE_015 : [EASY],
    TILE_015D : [EASY], # Duplicate of prev. tile
    TILE_016 : [EASY],
    TILE_017 : [EASY],
    TILE_017D : [EASY], # Duplicate of prev. tile
    TILE_018 : [EASY],
    TILE_019 : [EASY],
    TILE_019D : [EASY], # Duplicate of prev. tile
    TILE_020 : [EASY],
    TILE_020D : [EASY], # Duplicate of prev. tile
    TILE_021 : [EASY],
    TILE_022 : [EASY],
    TILE_023 : [EASY],
    TILE_024 : [EASY],
    TILE_025 : [EASY],
    TILE_025D : [EASY], # Duplicate of prev. tile
    TILE_026 : [EASY],
    TILE_026D : [EASY], # Duplicate of prev. tile
    TILE_027 : [EASY],
    TILE_028 : [EASY],
    TILE_029 : [EASY],
    TILE_030 : [EASY],
    TILE_031 : [EASY],
    TILE_032 : [EASY],
    TILE_033 : [EASY],
    TILE_034 : [EASY],
    TILE_035 : [EASY],
    TILE_036 : [EASY],
    TILE_037 : [EASY],
    TILE_038 : [EASY],
    TILE_039 : [EASY],
    TILE_040 : [EASY],
    TILE_040D : [EASY], # Duplicate of prev. tile
    TILE_041 : [EASY],
    TILE_042 : [EASY],
    TILE_043 : [EASY],
    TILE_044 : [EASY],
    TILE_045 : [EASY],
    TILE_046 : [EASY],
    TILE_046D : [EASY], # Duplicate of prev. tile
    TILE_047 : [EASY],
    TILE_048 : [EASY],
    TILE_049 : [EASY],
    TILE_049D : [EASY], # Duplicate of prev. tile
    TILE_050 : [EASY],
    TILE_051 : [EASY],
    TILE_052 : [EASY],
    TILE_053 : [EASY],
    TILE_054 : [EASY],
    TILE_054D : [EASY], # Duplicate of prev. tile
    TILE_055 : [EASY],
    TILE_055D : [EASY], # Duplicate of prev. tile
    TILE_056 : [EASY],
    TILE_056D : [EASY], # Duplicate of prev. tile
    TILE_057 : [EASY],
    TILE_057D : [EASY], # Duplicate of prev. tile
    TILE_058 : [EASY],
    TILE_059 : [EASY],
    TILE_060 : [EASY],
    TILE_060D : [EASY], # Duplicate of prev. tile
    TILE_061 : [EASY],
    TILE_062 : [EASY],
    TILE_063 : [EASY],
    TILE_064 : [EASY],
    TILE_065 : [EASY],
    TILE_066 : [EASY],
    TILE_067 : [EASY],
    TILE_068 : [EASY],
    TILE_069 : [EASY],
    TILE_070 : [EASY],
    TILE_071 : [EASY],
    TILE_071D : [EASY], # Duplicate of prev. tile
    TILE_072 : [EASY],
    TILE_072D : [EASY], # Duplicate of prev. tile
    TILE_073 : [EASY],
    TILE_074 : [EASY],
    TILE_074D : [EASY], # Duplicate of prev. tile
    TILE_074DD : [EASY], # Duplicate of 74
    TILE_075 : [EASY],
    TILE_076 : [EASY],
    TILE_076D : [EASY], # Duplicate of prev. tile
    TILE_076DD : [EASY], # Duplicate of 76
    TILE_077 : [EASY],
    TILE_078 : [EASY],
    TILE_079 : [EASY],
    TILE_080 : [EASY],
    TILE_081 : [EASY],
    TILE_082 : [EASY],
    TILE_083 : [EASY],
    TILE_084 : [EASY],
    TILE_085 : [EASY],
    TILE_086 : [EASY],
    TILE_087 : [EASY],
    TILE_088 : [EASY],
    TILE_089 : [EASY],
    TILE_089D : [EASY], # Duplicate of prev. tile
    TILE_090 : [EASY],
    TILE_091 : [EASY],
    TILE_091D : [EASY], # Duplicate of prev. tile
    TILE_092 : [EASY],
    TILE_093 : [EASY],
    TILE_094 : [EASY],
    TILE_094D : [EASY], # Duplicate of prev. tile
    TILE_095 : [EASY],
    TILE_095D : [EASY], # Duplicate of prev. tile
    TILE_096 : [EASY],
    TILE_096D : [EASY], # Duplicate of prev. tile
    TILE_097 : [EASY],
    TILE_098 : [EASY],
    TILE_099 : [EASY],
    TILE_100 : [EASY],
    TILE_101 : [EASY],
    TILE_102 : [EASY],
    TILE_103 : [EASY],
    TILE_103D : [EASY], # Duplicate of prev. tile
    TILE_104 : [EASY],
    TILE_105 : [EASY],
    TILE_106 : [EASY],
    TILE_107 : [EASY],
    TILE_108 : [EASY],
    TILE_109 : [EASY],
    TILE_110 : [EASY],
    TILE_110D : [EASY], # Duplicate of prev. tile
    TILE_111 : [EASY],
    TILE_112 : [EASY],
    TILE_113 : [EASY],
    TILE_114 : [EASY],
    TILE_114D : [EASY], # Duplicate of prev. tile
    TILE_115 : [EASY],
    TILE_115D : [EASY], # Duplicate of prev. tile
    TILE_116 : [EASY],
    TILE_117 : [EASY],
    TILE_117D : [EASY], # Duplicate of prev. tile
    TILE_118 : [EASY],
    TILE_118D : [EASY], # Duplicate of prev. tile
    TILE_119 : [EASY],
    TILE_120 : [EASY], 
    TILE_120D : [EASY], # Duplicate of prev. tile
    TILE_120DD : [EASY], # Duplicate of 120
    TILE_120DDD : [EASY], # Duplicate of 120
    TILE_121 : [EASY],
    TILE_122 : [EASY],
    TILE_123 : [EASY],
    TILE_124 : [EASY],
    TILE_125 : [EASY],
    TILE_125D : [EASY], # Duplicate of prev. tile
    TILE_126 : [EASY],
    TILE_127 : [EASY],
    TILE_128 : [EASY],
    TILE_128D : [EASY], # Duplicate of prev. tile
    TILE_129 : [EASY],
    TILE_130 : [EASY],
    TILE_131 : [EASY],
    TILE_131D : [EASY], # Duplicate of prev. tile
    TILE_132 : [EASY],
    TILE_133 : [EASY],
    TILE_134 : [EASY],
    TILE_134D : [EASY], # Duplicate of prev. tile
    TILE_135 : [EASY],
    TILE_136 : [EASY],
    TILE_136D : [EASY], # Duplicate of prev. tile
    TILE_137 : [EASY],
    TILE_138 : [EASY],
    TILE_138D : [EASY], # Duplicate of prev. tile
    TILE_139 : [EASY],
    TILE_140 : [EASY],
    TILE_141 : [EASY],
    TILE_142 : [EASY],
    TILE_143 : [EASY],
    TILE_144 : [EASY],
    TILE_145 : [EASY],
    TILE_146 : [EASY],
    TILE_147 : [EASY],
    TILE_148 : [EASY],
    TILE_149 : [EASY],
    TILE_150 : [EASY],
    TILE_151 : [EASY],
    TILE_152 : [EASY],
    TILE_153 : [EASY],
    TILE_153D : [EASY], # Duplicate of prev. tile
    TILE_154 : [EASY],
    TILE_154D : [EASY], # Duplicate of prev. tile
    TILE_155 : [EASY],
    TILE_156 : [EASY],
    TILE_157 : [EASY],
    TILE_158 : [EASY],
    TILE_159 : [EASY],
    TILE_160 : [EASY],
    TILE_161 : [EASY],
    TILE_162 : [EASY],
    TILE_163 : [EASY],
    TILE_164 : [EASY],
    TILE_165 : [EASY],
    TILE_166 : [EASY],
    TILE_167 : [EASY],
    TILE_168 : [EASY],
    TILE_169 : [EASY],
    TILE_170 : [EASY], 
    TILE_170D : [EASY], # Duplicate of prev. tile
    TILE_170DD : [EASY], # Duplicate of 170
    TILE_170DDD : [EASY], # Duplicate of 170
    TILE_171 : [EASY],
    TILE_171D : [EASY], # Duplicate of prev. tile
    TILE_171DD : [EASY], # Duplicate of 171
    TILE_171DDD : [EASY], # Duplicate of 171
    TILE_172 : [EASY],
    TILE_172D : [EASY], # Duplicate of prev. tile
    TILE_172DD : [EASY], # Duplicate of 172
    TILE_172DDD : [EASY], # Duplicate of 172
    TILE_173 : [EASY],
    TILE_174 : [EASY],
    TILE_175 : [EASY],
    TILE_176 : [EASY],
    TILE_177 : [EASY],
    TILE_178 : [EASY],
    TILE_179 : [EASY],
    TILE_180 : [EASY],
    TILE_181 : [EASY],
    TILE_181D : [EASY], # Duplicate of prev. tile
    TILE_181DD : [EASY], # Duplicate of 181
    TILE_181DDD : [EASY], # Duplicate of 181
    TILE_182 : [EASY],
    TILE_183 : [EASY],
    TILE_183D : [EASY], # Duplicate of prev. tile
    TILE_184 : [EASY],
    TILE_185 : [EASY],
    
}


"""Tile Weights

These can be used if `WEIGHTED` variable is set to true and will cause 
the tile choice to be skewed towards tiles with a higher value whenever possible.
"""
tileWeights = {
    TILE_001 : 1,
    TILE_002 : 1,
    TILE_003 : 1,
    TILE_004 : 1,
    TILE_005 : 1,
    TILE_006 : 1,
    TILE_007 : 1,
    TILE_008 : 1,
    TILE_009 : 1,
    TILE_010 : 1,
    TILE_011 : 1,
    TILE_012 : 1,
    TILE_013 : 1,
    TILE_014 : 1,
    TILE_015 : 1,
    TILE_016 : 1,
    TILE_017 : 1,
    TILE_018 : 1,
    TILE_019 : 1,
    TILE_020 : 1,
    TILE_021 : 1,
    TILE_022 : 1,
    TILE_023 : 1,
    TILE_024 : 1,
    TILE_025 : 1,
    TILE_026 : 1,
    TILE_027 : 1,
    TILE_028 : 1,
    TILE_029 : 1,
    TILE_030 : 1,
    TILE_031 : 1,
    TILE_032 : 1,
    TILE_033 : 1,
    TILE_034 : 1,
    TILE_035 : 1,
    TILE_036 : 1,
    TILE_037 : 1,
    TILE_038 : 1,
    TILE_039 : 1,
    TILE_040 : 1,
    TILE_041 : 1,
    TILE_042 : 1,
    TILE_043 : 1,
    TILE_044 : 1,
    TILE_045 : 1,
    TILE_046 : 1,
    TILE_047 : 1,
    TILE_048 : 1,
    TILE_049 : 1,
    TILE_050 : 1,
    TILE_051 : 1,
    TILE_052 : 1,
    TILE_053 : 1,
    TILE_054 : 1,
    TILE_055 : 1,
    TILE_056 : 1,
    TILE_057 : 1,
    TILE_058 : 1,
    TILE_059 : 1,
    TILE_060 : 1,
    TILE_061 : 1,
    TILE_062 : 1,
    TILE_063 : 1,
    TILE_064 : 1,
    TILE_065 : 1,
    TILE_066 : 1,
    TILE_067 : 1,
    TILE_068 : 1,
    TILE_069 : 1,
    TILE_070 : 1,
    TILE_071 : 1,
    TILE_072 : 1,
    TILE_073 : 1,
    TILE_074 : 1,
    TILE_075 : 1,
    TILE_076 : 1,
    TILE_077 : 1,
    TILE_078 : 1,
    TILE_079 : 1,
    TILE_080 : 1,
    TILE_081 : 1,
    TILE_082 : 1,
    TILE_083 : 1,
    TILE_084 : 1,
    TILE_085 : 1,
    TILE_086 : 1,
    TILE_087 : 1,
    TILE_088 : 1,
    TILE_089 : 1,
    TILE_090 : 1,
    TILE_091 : 1,
    TILE_092 : 1,
    TILE_093 : 1,
    TILE_094 : 1,
    TILE_095 : 1,
    TILE_096 : 1,
    TILE_097 : 1,
    TILE_098 : 1,
    TILE_099 : 1,
    TILE_100 : 1,
    TILE_101 : 1,
    TILE_102 : 1,
    TILE_103 : 1,
    TILE_104 : 1,
    TILE_105 : 1,
    TILE_106 : 1,
    TILE_107 : 1,
    TILE_108 : 1,
    TILE_109 : 1,
    TILE_110 : 1,
    TILE_111 : 1,
    TILE_112 : 1,
    TILE_113 : 1,
    TILE_114 : 1,
    TILE_115 : 1,
    TILE_116 : 1,
    TILE_117 : 1,
    TILE_118 : 1,
    TILE_119 : 1,
    TILE_120 : 1,
    TILE_121 : 1,
    TILE_122 : 1,
    TILE_123 : 1,
    TILE_124 : 1,
    TILE_125 : 1,
    TILE_126 : 1,
    TILE_127 : 1,
    TILE_128 : 1,
    TILE_129 : 1,
    TILE_130 : 1,
    TILE_131 : 1,
    TILE_132 : 1,
    TILE_133 : 1,
    TILE_134 : 1,
    TILE_135 : 1,
    TILE_136 : 1,
    TILE_137 : 1,
    TILE_138 : 1,
    TILE_139 : 1,
    TILE_140 : 1,
    TILE_141 : 1,
    TILE_142 : 1,
    TILE_143 : 1,
    TILE_144 : 1,
    TILE_145 : 1,
    TILE_146 : 1,
    TILE_147 : 1,
    TILE_148 : 1,
    TILE_149 : 1,
    TILE_150 : 1,
    TILE_151 : 1,
    TILE_152 : 1,
    TILE_153 : 1,
    TILE_154 : 1,
    TILE_155 : 1,
    TILE_156 : 1,
    TILE_157 : 1,
    TILE_158 : 1,
    TILE_159 : 1,
    TILE_160 : 1,
    TILE_161 : 1,
    TILE_162 : 1,
    TILE_163 : 1,
    TILE_164 : 1,
    TILE_165 : 1,
    TILE_166 : 1,
    TILE_167 : 1,
    TILE_168 : 1,
    TILE_169 : 1,
    TILE_170 : 1,
    TILE_171 : 1,
    TILE_172 : 1,
    TILE_173 : 1,
    TILE_174 : 1,
    TILE_175 : 1,
    TILE_176 : 1,
    TILE_177 : 1,
    TILE_178 : 1,
    TILE_179 : 1,
    TILE_180 : 1,
    TILE_181 : 1,
    TILE_182 : 1,
    TILE_183 : 1,
    TILE_184 : 1,
    TILE_185 : 1,
    
    # Duplicates:
    TILE_005D : 1,
    TILE_015D : 1,
    TILE_017D : 1, 
    TILE_019D : 1,
    TILE_020D : 1,
    TILE_025D : 1,
    TILE_026D : 1,
    TILE_040D : 1,
    TILE_046D : 1,
    TILE_049D : 1,
    TILE_054D : 1,
    TILE_055D : 1,
    TILE_056D : 1,
    TILE_057D : 1, 
    TILE_060D : 1,
    TILE_071D : 1,
    TILE_072D : 1,
    TILE_074D : 1,
    TILE_074DD : 1,
    TILE_076D : 1,
    TILE_076DD : 1,
    TILE_089D : 1,
    TILE_091D : 1,
    TILE_094D : 1,
    TILE_095D : 1,
    TILE_096D : 1,
    TILE_103D : 1,
    TILE_110D : 1,
    TILE_114D : 1,
    TILE_115D : 1,
    TILE_117D : 1,
    TILE_118D : 1,
    TILE_120D : 1,
    TILE_120DD : 1,
    TILE_120DDD : 1,
    TILE_125D : 1,
    TILE_128D : 1,
    TILE_131D : 1,
    TILE_134D : 1,
    TILE_136D : 1,
    TILE_138D : 1,
    TILE_153D : 1,
    TILE_154D : 1,
    TILE_170D : 1,
    TILE_170DD : 1,
    TILE_170DDD : 1,
    TILE_171D : 1,
    TILE_171DD : 1,
    TILE_171DDD : 1,
    TILE_172D : 1,
    TILE_172DD : 1, 
    TILE_172DDD : 1,
    TILE_181D : 1,
    TILE_181DD : 1,
    TILE_181DDD : 1,
    TILE_183D : 1,

}

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

}
