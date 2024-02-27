import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import warnings
warnings.filterwarnings("ignore")
##

Nlines = 3
Ncols = 6
N = Nlines*Ncols

territory = ['forest', 'desert', 'lake', 'mountain', 'swamp']
col_ter = np.array(['tab:{}'.format(col) for col in['green', 'orange', 'blue', 'grey', 'purple']])

animal = ['', 'bear', 'cougar']

obj_form = ['', '^', 'o']
obj_col = ['b', 'g', 'w', 'k']
obj = ['{}_{}'.format(form, col) for form in obj_form[1:] for col in obj_col]
obj.insert(0, '')

##

name_lon = "lon"
name_lat = "lat"
name_territory = "territory"
name_animal = "animal"
name_obstacle = "obstacle"
name_line = 'line'
name_col = 'col'

##

positions = np.zeros((3,6,2))
dx = 3/2
dy = np.sqrt(3)

for col in range(Ncols):
    positions[:,col,1] = col * dx

for col in range(0, Ncols, 2):
    positions[:,col,0] = dy/2

for line in range(1, Nlines):
    positions[line,:,0] = positions[0,:,0] + line*dy


dict_arr =	{
    name_lon: positions[:,:,1].ravel(),
    name_lat: positions[:,:,0].ravel(),
    name_territory: N*[0],
    name_animal: N*[0],
    name_obstacle: N*[0],
    # name_territory: N*[[territory[0], col_ter[0]]],
    # name_animal: N*[animal[0]],
    # name_obstacle: N*[[obj_form[0], obj_col[0]]],
}

##

iterables = [range(3), range(6)]
# XX, YY = np.meshgrid(xs, ys)
multi_ind = pd.MultiIndex.from_product(iterables, names=[name_line, name_col])

df0 = pd.DataFrame(data=dict_arr, index = multi_ind)
df0[name_animal] = ''
df0[name_obstacle] = ''

boards = []

##

def fun_attr(df, ter_inds, ter_which):
    # df[name_territory][ter_inds] = len(ter_inds) * [[territory[ter_which], col_ter[ter_which]]]
    df[name_territory][ter_inds] = ter_which

## 1
df = df0.copy()
df[name_animal] = ''

ter_inds = [[2,4], [1,4], [2,5], [1,5], [0,5]]
fun_attr(df, ter_inds, 0)

ter_inds = [[0,2], [1,3], [0,3], [0,4]]
fun_attr(df, ter_inds, 1)

ter_inds = [[2,0], [2,1], [2,2], [1,2], [2,3]]
fun_attr(df, ter_inds, 2)

ter_inds = [[1,0], [0,0], [1,1], [0,1]]
fun_attr(df, ter_inds, 4)


anim_inds = [[0,3], [0,4], [0,5]]
df[name_animal][anim_inds] = 1

boards.append(df)

## 2
df = df0.copy()
df[name_animal] = ''

ter_inds = [[2,1], [2,2], [1,2], [2,3], [2,4], [2,5]]
fun_attr(df, ter_inds, 0)

ter_inds = [[1,3], [1,4], [1,5], [0,5]]
fun_attr(df, ter_inds, 1)

ter_inds = [[0,1], [0,2], [0,3], [0,4]]
fun_attr(df, ter_inds, 3)

ter_inds = [[2,0], [1,0], [0,0], [1,1]]
fun_attr(df, ter_inds, 4)


anim_inds = [[2,0], [2,1], [2,2]]
df[name_animal][anim_inds] = 2

boards.append(df)

## 3
df = df0.copy()
df[name_animal] = ''

ter_inds = [[2,2], [1,2], [2,3], [2,4]]
fun_attr(df, ter_inds, 0)

ter_inds = [[1,4], [0,4], [2,5], [1,5], [0,5]]
fun_attr(df, ter_inds, 2)

ter_inds = [[0,0], [0,1], [0,2], [1,3], [0,3]]
fun_attr(df, ter_inds, 3)

ter_inds = [[2,0], [1,0], [2,1], [1,1]]
fun_attr(df, ter_inds, 4)


anim_inds = [[1,0], [0,0], [1,1]]
df[name_animal][anim_inds] = 2

boards.append(df)

## 4
df = df0.copy()
df[name_animal] = ''

ter_inds = [[0,3], [0,4], [0,5]]
fun_attr(df, ter_inds, 0)

ter_inds = [[2,0], [1,0], [0,0], [2,1], [1,1], [0,1], [0,2]]
fun_attr(df, ter_inds, 1)

ter_inds = [[1,3], [1,4], [1,5]]
fun_attr(df, ter_inds, 2)

ter_inds = [[2,2], [1,2], [2,3], [2,4], [2,5]]
fun_attr(df, ter_inds, 3)


anim_inds = [[1,5], [0,5]]
df[name_animal][anim_inds] = 2

boards.append(df)

## 5
df = df0.copy()
df[name_animal] = ''

ter_inds = [[0,0], [1,1], [0,1], [1,2]]
fun_attr(df, ter_inds, 1)

ter_inds = [[0,2], [1,3], [0,3], [0,4], [0,5]]
fun_attr(df, ter_inds, 2)

ter_inds = [[2,3], [2,4], [1,4], [2,5], [1,5]]
fun_attr(df, ter_inds, 3)

ter_inds = [[2,0], [1,0], [2,1], [2,2]]
fun_attr(df, ter_inds, 4)


anim_inds = [[0,4], [1,5], [0,5]]
df[name_animal][anim_inds] = 1

boards.append(df)

## 6
df = df0.copy()
df[name_animal] = ''

ter_inds = [[1,4], [2,5], [1,5], [0,5]]
fun_attr(df, ter_inds, 0)

ter_inds = [[2,0], [2,1]]
fun_attr(df, ter_inds, 1)

ter_inds = [[0,1], [0,2], [0,3], [0,4]]
fun_attr(df, ter_inds, 2)

ter_inds = [[1,0], [0,0], [1,1]]
fun_attr(df, ter_inds, 3)

ter_inds = [[2,2], [1,2], [2,3], [1,3], [2,4]]
fun_attr(df, ter_inds, 4)


anim_inds = [[2,0], [1,0]]
df[name_animal][anim_inds] = 1

boards.append(df)

##

order = [3, 6, 1, 4, 5, 2]
bool_transpose = [1, 1, 0, 1, 0, 1]

for ind, board in enumerate(boards):
    ind_order = order.index(ind+1)
    if bool_transpose[ind_order]:
        board[name_lon] = board[name_lon].max() - board[name_lon]
        board[name_lat] = board[name_lat].max() - board[name_lat]
    board[name_lat] = board[name_lat] + (2-(ind_order%3)) * Nlines*dy
    board[name_lon] = board[name_lon] + (ind_order//3) * Ncols*dx

# boards_ordered = [boards[i-1] for i in order]
df = pd.concat(boards)

##

# ind_board = 5
# df = boards[ind_board]
s = 2500
lw = 3
# s = 1

plt.close('all')

# col_tmp = boards[ind_board][name_territory].values
# col_arr = [col_tmp[x][1] for x in range(col_tmp.size)]

fig = plt.figure()
ax = fig.add_subplot()
plt.scatter(x = df[name_lon].values, y = df[name_lat].values, s = s, c = col_ter[df[name_territory].values], marker = 'H')

size = np.ma.masked_where(df[name_animal]!=1, np.full((df.shape[0],), s))
plt.scatter(x = df[name_lon].values, y = df[name_lat].values, s = size, marker = 'H', facecolors="None", edgecolors = 'k', linestyle = '--', linewidth = lw)

size = np.ma.masked_where(df[name_animal]!=2, np.full((df.shape[0],), s))
plt.scatter(x = df[name_lon].values, y = df[name_lat].values, s = size, marker = 'H', facecolors="None", edgecolors = 'r', linewidth = lw)

# plt.xlim(-1, 9)
# plt.ylim(-1, 9)
ax.set_aspect('equal')

siz = 9
fig = plt.gcf()
fig.set_size_inches(siz, siz)

plt.show()

## BIN

# dict_tmp =	{
#     name_lon: 0,
#     name_lat: 0,
#     name_territory: territory[0],
#     name_animal: animal[0],
#     name_obstacle: [obj_form[0], obj_col[0]],
# }

# board1 = [[dict_tmp for _ in range(Ncols)] for i in range(Nlines)]
# for line in range(Nlines):
#     for col in range(Ncols):
#         board1[line][col][name_lon] = positions[line, col, 1]
#         board1[line][col][name_lat] = positions[line, col, 0]
#
#
# def fun_attr(board, ter_inds, ter_which):
#     for line,col in ter_inds:
#         board[line][col][name_territory] = territory[ter_which]
#
#
# ter_inds = [[2,4], [1,4], [2,5], [1,5], [0,5]]
# fun_attr(board1, ter_inds, 0)
#
# ter_inds = [[0,2], [1,3], [0,3], [0,4]]
# fun_attr(board1, ter_inds, 1)
#
# ter_inds = [[2,0], [2,1], [2,2], [1,2], [2,3]]
# fun_attr(board1, ter_inds, 2)
#
# ter_inds = []
# fun_attr(board1, ter_inds, 3)
#
# ter_inds = [[1,0], [0,0], [1,1], [0,1]]
# fun_attr(board1, ter_inds, 4)