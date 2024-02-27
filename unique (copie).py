import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import itertools
import copy

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
df[name_index] = range(df.shape[0])

##

clues_fun = all_clues()
name_clues = [i[0] for i in clues_fun]

for ind_clue in range(len(clues_fun)):
    label, type_col, possibs, d = clues_fun[ind_clue]
    print(label)
    clue_column(label, type_col, possibs, d, df)

##

if bool_diff:
    for label in name_clues:
        df['not_'+label] = ~df[label]

##

print()
list_big = []
for Nclues in range(2,6):
    print(Nclues)
    list_small = []
    for clues in itertools.combinations(df.columns[5:], Nclues):
        tmp = df[list(clues)].product(axis = 1)
        if tmp.sum() == 1:

            bol_tmp = True
            for clues_old in [item for sublist in list_big for item,_ in sublist]:
                if set(clues_old) <= set(clues):
                    bol_tmp = False
            if bol_tmp:
                ind_tmp = df[name_index][tmp==1].values
                list_small.append([clues, ind_tmp[0]])
                # print(df[tmp==1][['lon', 'lat', 'index1']].values)

    list_big.append(list_small)

##

l = copy.deepcopy(list_big)
for Nclues in range(4):

    tmp_range = range(len(l[Nclues]))
    list_ind = [l[Nclues][i][1] for i in tmp_range]
    # print(list_ind)

    num1 = 0
    while num1 < len(l[Nclues]):
        index1 = list_ind[num1]
    # for num1, index1 in enumerate(list_ind):
        list_tmp = []
        for num2 in range(num1+1, len(list_ind)):
            index2 = list_ind[num2]
            if index2 == index1:
                list_tmp.append(num2)
        if list_tmp:
            list_tmp.insert(0, num1)
            for num in list_tmp[::-1]:
                l[Nclues].pop(num)
                list_ind.pop(num)
        else:
            num1 += 1


# for i in tmp_range:
#     print(list_big[Nclues][i])
# print()
for Nclues in range(4):
    for i in range(len(l[Nclues])):
        print(l[Nclues][i])
    print()

##


# def rec_small(clues, lis):
#     clues = list(clues)
#     nb_sol = df[clues].product(axis = 1).sum()
#     if nb_sol < 2:
#         bool_nm1 = False
#         if len(clues) > 2:
#             for clue in clues:
#                 clues_small = [i for i in clues if i != clue]
#                 nb_sol_nm1, lis = rec_small(clues_small, lis)
#                 if nb_sol_nm1 == 1:
#                     bool_nm1 = True
#         if nb_sol == 1 and bool_nm1 == False:
#             lis[len(clues)-2].append(clues)
#     return nb_sol, lis
#
#
# Nclues = 5
# lis = [[],[],[],[]]
# for clues in itertools.combinations(df.columns[5:], Nclues):
#     print(clues)
#     _, lis = rec_small(clues, lis)
