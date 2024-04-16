import os
import re
from collections import Counter

def variety(dir, amount):
    """"""
    
    # tiles_used = dict()
    seed = []

   
    for f in os.listdir(dir):

        filename = str(f)

        seed = seed + re.findall(r'\d+', filename)

    tiles_appearance = dict(Counter(seed))
    # print(type(seed))
    ranked =sorted(tiles_appearance.items(), key=lambda x:x[1])
    # print(ranked)

    for i in range(len(ranked)):
        print("tileID:", ranked[i][0],"occ.:",ranked[i][1]) 
            

        
    



        



amount_of_levels = 1000
directory = '../WFCinPythonforPlatformers/result_images'
variety(directory, amount_of_levels)