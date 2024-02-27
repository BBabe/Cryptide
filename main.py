import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

## à 1 des forêts

bols =['lake_swamp', 'desert', 'o', 'cougar', 'w']

clues_fun = all_clues()
name_clues = [i[0] for i in clues_fun]

for bol in bols:
    ind_clue = name_clues.index(bol)
    bol, type_col, possibs, d = clues_fun[ind_clue]
    print(bol)
    clue_column(bol, type_col, possibs, d, df)


##
plt.close('all')
s = 2000
lw = 3

fig = plt.figure()
ax = fig.add_subplot()

plt.scatter(x = df[name_lon].values, y = df[name_lat].values, s = s, c = col_ter[df[name_territory].values], alpha = 0.8, marker = 'H')

size = np.ma.masked_where(df[name_animal]!=1, np.full((df.shape[0],), s))
plt.scatter(x = df[name_lon].values, y = df[name_lat].values, s = size, marker = 'H', facecolors="None", edgecolors = 'k', linestyle = '--', linewidth = lw)

size = np.ma.masked_where(df[name_animal]!=2, np.full((df.shape[0],), s))
plt.scatter(x = df[name_lon].values, y = df[name_lat].values, s = size, marker = 'H', facecolors="None", edgecolors = 'r', linewidth = lw)

df_obj = df[df[name_obstacle]!=0]
# markers = [df_obj[name_obstacle].iloc[i][0] for i in range(df_obj.shape[0])]
# colors = [df_obj[name_obstacle].iloc[i][-1] for i in range(df_obj.shape[0])]
markers = [objs[df_obj[name_obstacle].iloc[i]][0] for i in range(df_obj.shape[0])]
colors = [objs[df_obj[name_obstacle].iloc[i]][-1] for i in range(df_obj.shape[0])]
for lon, lat, col, mark in zip(df_obj[name_lon], df_obj[name_lat], colors, markers):
    plt.scatter(x = lon, y = lat, c = col, s = s/3, marker = mark)


for bol in bols:
    size = np.ma.masked_where(df[bol]==True, np.full((df.shape[0],), s))
    plt.scatter(x = df[name_lon].values, y = df[name_lat].values, s = size, hatch = 'xxx', alpha = 0)


plt.xticks(np.arange(0, 17, 1.5), range(1,13))
plt.yticks(np.arange(np.sqrt(3)/4, 15, np.sqrt(3)), range(1,10))
# plt.grid(True)

ax.set_aspect('equal')
siz = 9
fig = plt.gcf()
fig.set_size_inches(siz, siz)


plt.show()
