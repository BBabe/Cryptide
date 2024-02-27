import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import itertools

from boards import *
from indices import *

import warnings
warnings.filterwarnings("ignore")
##

bool_diff = 0
order = [6,5,3,4,1,2]
bool_transpose = [0,1,1,0,0,1]

# a = np.array([[3,4],[6,5],[1,2]])
# print(a, ' --> ', list(a.transpose().ravel()))


obj_pos = [[]]
obj_pos.append([3, [0,3]]) # white triangle '^_w'
obj_pos.append([3, [0,5]]) # blue triangle '^_b'
obj_pos.append([6, [1,5]]) # green triangle '^_g'
if bool_diff:
    obj_pos.append([4, [2,1]]) # black triangle '^_k'
else:
    obj_pos.append([])

obj_pos.append([6, [0,2]]) # white cylinder 'o_w'
obj_pos.append([5, [0,4]]) # blue cylinder 'o_b'
obj_pos.append([5, [0,0]]) # green cylinder 'o_g'
if bool_diff:
    obj_pos.append([2, [1,2]]) # black cylinder 'o_k'
else:
    obj_pos.append([])

##

boards_obj = [[ind_obj for ind_obj in range(Nobjs) if (obj_pos[ind_obj] and obj_pos[ind_obj][0] == ind)] for ind in range(1,7)]

for ind, board in enumerate(boards):
    ind_order = order.index(ind+1)

    if bool_transpose[ind_order]:
        board[name_lon] = board[name_lon].max() - board[name_lon]
        board[name_lat] = board[name_lat].max() - board[name_lat]
        index_tmp = [tuple([2,5] - np.array(board.index[i])) for i in range(board.shape[0])]
        board.index = pd.MultiIndex.from_tuples(index_tmp, names = board.index.names)

    board[name_lat] = board[name_lat] + (2-(ind_order%3)) * Nlines*dy
    board[name_lon] = board[name_lon] + (ind_order//3) * Ncols*dx

    list_obj = boards_obj[ind]
    if list_obj:
        for ind_obj in list_obj:
            board[name_obstacle][tuple(obj_pos[ind_obj][1])] = objs_nums[ind_obj]

df = pd.concat(boards)

##

clues_fun = all_clues()
name_clues = [i[0] for i in clues_fun]

for ind_clue in range(len(clues_fun)):
    bol, type_col, possibs, d = clues_fun[ind_clue]
    print(bol)
    clue_column(bol, type_col, possibs, d, df)

##

if bool_diff:
    for col in name_clues:
        df['not_'+col] = ~df[col]

##

cols = df.columns[5:]
for i in range(len(cols)):
    for j in range(i+1, len(cols)):
        bols = [cols[i], cols[j]]
        tmp = df[bols].product(axis = 1)
        if tmp.sum() == 1:
            print(bols, df[tmp==1][['lon', 'lat']].values)
        elif tmp.sum() > 1:
            for k in range(j+1, len(cols)):
                bols = [cols[i], cols[j], cols[k]]
                tmp = df[bols].product(axis = 1)
                if tmp.sum() == 1:
                    print(bols, df[tmp==1][['lon', 'lat']].values)


##

Nclues = 2
for bols in itertools.combinations(df.columns[5:], Nclues):

for i in itertools.combinations(range(5), 3):
    print(i)
