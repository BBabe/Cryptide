import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings("ignore")
##

Nlines = 3
Ncols = 6
Ncells = Nlines*Ncols

territory = ['forest', 'desert', 'lake', 'mountain', 'swamp']
col_ter = np.array(['tab:{}'.format(col) for col in['green', 'orange', 'blue', 'grey', 'purple']])

animal = ['', 'bear', 'cougar']

obj_form = ['', '^', 'o']
obj_col = ['w', 'b', 'g', 'k']
objs = ['{}_{}'.format(form, col) for form in obj_form[1:] for col in obj_col]
objs.insert(0, '')
Nobjs = len(objs)
objs_nums = range(Nobjs)

##

name_lon = "lon"
name_lat = "lat"
name_territory = "territory"
name_animal = "animal"
name_obstacle = "obstacle"
name_line = 'line'
name_col = 'col'
name_index = 'index1'

##

positions = np.zeros((3,6,2))
dx = 3/2
dy = np.sqrt(3)
eps = min(dx,dy)/1000

for col in range(Ncols):
    positions[:,col,1] = col * dx

for col in range(0, Ncols, 2):
    positions[:,col,0] = dy/2

for line in range(1, Nlines):
    positions[line,:,0] = positions[0,:,0] + line*dy


dict_small = {
    name_lon: positions[:,:,1].ravel(),
    name_lat: positions[:,:,0].ravel(),
    name_territory: Ncells*[0]
}

##

iterables = [range(3), range(6)]
multi_ind = pd.MultiIndex.from_product(iterables, names=[name_line, name_col])

df0 = pd.DataFrame(data=dict_small, index = multi_ind)
df0[name_animal] = 0
df0[name_obstacle] = 0

boards = []

## 1
df = df0.copy()

ter_inds = [[2,4], [1,4], [2,5], [1,5], [0,5]]
df[name_territory][ter_inds] = 0

ter_inds = [[0,2], [1,3], [0,3], [0,4]]
df[name_territory][ter_inds] = 1

ter_inds = [[2,0], [2,1], [2,2], [1,2], [2,3]]
df[name_territory][ter_inds] = 2

ter_inds = [[1,0], [0,0], [1,1], [0,1]]
df[name_territory][ter_inds] = 4


anim_inds = [[0,3], [0,4], [0,5]]
df[name_animal][anim_inds] = 1

boards.append(df)

## 2
df = df0.copy()
df[name_animal] = 0

ter_inds = [[2,1], [2,2], [1,2], [2,3], [2,4], [2,5]]
df[name_territory][ter_inds] = 0

ter_inds = [[1,3], [1,4], [1,5], [0,5]]
df[name_territory][ter_inds] = 1

ter_inds = [[0,1], [0,2], [0,3], [0,4]]
df[name_territory][ter_inds] = 3

ter_inds = [[2,0], [1,0], [0,0], [1,1]]
df[name_territory][ter_inds] = 4


anim_inds = [[2,0], [2,1], [2,2]]
df[name_animal][anim_inds] = 2

boards.append(df)

## 3
df = df0.copy()
df[name_animal] = 0

ter_inds = [[2,2], [1,2], [2,3], [2,4]]
df[name_territory][ter_inds] = 0

ter_inds = [[1,4], [0,4], [2,5], [1,5], [0,5]]
df[name_territory][ter_inds] = 2

ter_inds = [[0,0], [0,1], [0,2], [1,3], [0,3]]
df[name_territory][ter_inds] = 3

ter_inds = [[2,0], [1,0], [2,1], [1,1]]
df[name_territory][ter_inds] = 4


anim_inds = [[1,0], [0,0], [1,1]]
df[name_animal][anim_inds] = 2

boards.append(df)

## 4
df = df0.copy()
df[name_animal] = 0

ter_inds = [[0,3], [0,4], [0,5]]
df[name_territory][ter_inds] = 0

ter_inds = [[2,0], [1,0], [0,0], [2,1], [1,1], [0,1], [0,2]]
df[name_territory][ter_inds] = 1

ter_inds = [[1,3], [1,4], [1,5]]
df[name_territory][ter_inds] = 2

ter_inds = [[2,2], [1,2], [2,3], [2,4], [2,5]]
df[name_territory][ter_inds] = 3


anim_inds = [[1,5], [0,5]]
df[name_animal][anim_inds] = 2

boards.append(df)

## 5
df = df0.copy()
df[name_animal] = 0

ter_inds = [[0,0], [1,1], [0,1], [1,2]]
df[name_territory][ter_inds] = 1

ter_inds = [[0,2], [1,3], [0,3], [0,4], [0,5]]
df[name_territory][ter_inds] = 2

ter_inds = [[2,3], [2,4], [1,4], [2,5], [1,5]]
df[name_territory][ter_inds] = 3

ter_inds = [[2,0], [1,0], [2,1], [2,2]]
df[name_territory][ter_inds] = 4


anim_inds = [[0,4], [1,5], [0,5]]
df[name_animal][anim_inds] = 1

boards.append(df)

## 6
df = df0.copy()
df[name_animal] = 0

ter_inds = [[1,4], [2,5], [1,5], [0,5]]
df[name_territory][ter_inds] = 0

ter_inds = [[2,0], [2,1]]
df[name_territory][ter_inds] = 1

ter_inds = [[0,1], [0,2], [0,3], [0,4]]
df[name_territory][ter_inds] = 2

ter_inds = [[1,0], [0,0], [1,1]]
df[name_territory][ter_inds] = 3

ter_inds = [[2,2], [1,2], [2,3], [1,3], [2,4]]
df[name_territory][ter_inds] = 4


anim_inds = [[2,0], [1,0]]
df[name_animal][anim_inds] = 1

boards.append(df)
