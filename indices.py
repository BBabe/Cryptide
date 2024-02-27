import pandas as pd
import numpy as np
from boards import *
##

bols =['bear', 'forest_desert', 'green']


def fun_dist(df1, ind1, df2, ind2):
    lon1, lat1 = df1[[name_lon, name_lat]].iloc[ind1]
    lon2, lat2 = df2[[name_lon, name_lat]].iloc[ind2]
    return np.sqrt((lon2-lon1)**2 + (lat2-lat1)**2)


def clue_column(bol, type_col, possibs, d, df):
    col_bol = df[type_col].isin(possibs)
    df[bol] = False
    df_tmp = df[col_bol]
    df[bol][col_bol] = True
    if d:
        dist = (dy+eps)*d
        for i in range(df_tmp.shape[0]):
            lon1, lat1 = df_tmp[[name_lon, name_lat]].iloc[i]
            sphere = np.sqrt((lon1-df[name_lon])**2 + (lat1-df[name_lat])**2) < dist
            df[bol][sphere] = True


def all_clues():
    lis = []

    dist = 0
    for i, ter1 in enumerate(territory):
        for j in range(i+1, len(territory)):
            ter2 = territory[j]
            label = '{}_{}'.format(ter1, ter2)
            type_col = name_territory
            possibs = [i,j]

            lis.append([label, type_col, possibs, dist])

    dist = 1
    for i, ter in enumerate(territory):
        label = ter
        type_col = name_territory
        possibs = [i]

        lis.append([label, type_col, possibs, dist])
    lis.append([name_animal[:-2], name_animal, [1,2], dist])

    dist = 2
    for i, shape in enumerate(obj_form[1:]):
        label = shape
        type_col = name_obstacle
        possibs = [4*i + j for j in [1,2,3,4]]

        lis.append([label, type_col, possibs, dist])
    for i, anim in enumerate(animal[1:]):
        label = anim
        type_col = name_animal
        possibs = [i+1]

        lis.append([label, type_col, possibs, dist])

    dist = 3
    for i, color in enumerate(obj_col):
        label = color
        type_col = name_obstacle
        possibs = [i+1, i+5]

        lis.append([label, type_col, possibs, dist])

    return lis

##

# for li in all_clues():
#     print(li)