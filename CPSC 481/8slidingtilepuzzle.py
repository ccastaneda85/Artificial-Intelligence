from search import *

eight_puzzle = EightPuzzle((1, 2, 3, 5, 7, 4, 8, 6, 0)) # <- change this

if __name__ == '__main__':
    print(breadth_first_graph_search(eight_puzzle).solution())
    exit()