from RBFS_search import recursive_best_first_search
from puzzle import Puzzle

state=[[1, 3, 4,
        8, 6, 2,
        7, 0, 5],

       [2, 8, 1,
        0, 4, 3,
        7, 6, 5],

       [2, 8, 1,
        4, 6, 3,
        0, 7, 5]]

for i in range(0,3):
    Puzzle.num_of_instances = 0
    RBFS = recursive_best_first_search(state[i])
    print('Estado numero', i+1)
    print('Movimientos para estado final:',RBFS)
    print('Numero de Movimientos:', Puzzle.num_of_instances)
    print('############################################')
