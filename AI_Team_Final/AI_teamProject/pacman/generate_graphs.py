import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

table1 = [['Maze Type', 'Bidirectional-MM', 'Bidirectional-MM0', 'A*', 'UCS', 'BFS', 'DFS'],
          ['Small Maze', 45, 54, 53, 92, 92, 59],
          ['Medium Maze', 177, 185, 221, 269, 269, 146],
          ['Big Maze', 610, 608, 549, 620, 620, 390],
          ['Tiny Corners', 205, 210, 199, 252, 252, 51],
          ['Medium Corners', 797, 818, 1136, 1966, 1966, 371],
          ['Big Corners', 2668, 2705, 4380, 7949, 7949, 504]]
print("Nodes expanded for default mazes:")
print(tabulate(table1))

table2 = [['Maze Type', 'Bidirectional-MM', 'Bidirectional-MM0', 'A*', 'UCS', 'BFS', 'DFS'],
                    ['Small Maze', 19, 19, 19, 19, 19, 49],
                   ['Medium Maze', 68, 68, 68, 68, 68, 130],
                   ['Big Maze', 210, 210, 210, 210, 210, 210],
                   ['Tiny Corners', 33, 33, 28, 28, 28, 47],
                   ['Medium Corners', 106, 106, 106, 106, 106, 221],
                   ['Big Corners', 162, 162, 162, 162, 162, 302]]
print("Path Cost for default mazes:")
print(tabulate(table1))

table3 = [['Maze Type', 'Start Node', 'Goal Nodes', 'Bidirectional-MM', 'Bidirectional-MM0', 'A*', 'UCS', 'BFS', 'DFS'],
          ['bdMaze', '(35, 1)', '(1,1)', 233, 222, 244, 375, 375, 393],
          ['bdMaze1', '(35, 1)', '(1,1)', 600, 598, 539, 610, 610, 388],
          ['bdMaze2', '(35, 1)', '(1,1)',524, 537, 586, 633, 633, 335],
          ['bdMaze3', '(35, 1)', '(1,1)',303, 301, 300, 612, 612, 335],
          ['bdMaze4', '(33, 19)', '(1,1)',282, 274, 312, 582, 582, 325],
          ['bigMaze', '(35, 1)', '(1,1)',610, 608, 549, 620, 620, 568],
          ['bigMaze1', '(33, 27)', '(1,1)',315, 333, 388, 666, 666, 390],
          ['bigMaze2', '(29, 33)', '(1,1)',242, 249, 278, 658, 658, 437],
          ['bigMaze3', '(18, 27)', '(1,1)',362, 362, 315, 431, 431, 466],
          ['bigMaze4', '(33, 27)', '(1,1)',273, 277, 316, 628, 628, 355],
          ['bigMaze5', '(19, 35)', '(1,1)',263, 279, 313, 466, 466, 267],
          ['bigMaze6', '(8, 1)', '(1,1)',86, 194, 195, 350, 350, 424],
          ['bigMaze7', '(32, 27)', '(1,1)',531, 539, 497, 623, 623, 283],
          ['megaMaze', '(68, 70)', '(1,1)',1922, 1934, 1154, 2639, 2639, 2331]]
print("Nodes expanded for Custom mazes:")
print(tabulate(table3))

table4 = [['Maze Type', 'Start Node', 'Goal Nodes', 'Bidirectional-MM', 'Bidirectional-MM0', 'A*', 'UCS', 'BFS', 'DFS'],
          ['bdMaze', '(35, 1)', '(1,1)', 74, 74, 74, 74, 74, 214],
          ['bdMaze1', '(35, 1)', '(1,1)', 210, 210, 210, 210, 210, 210],
          ['bdMaze2', '(35, 1)', '(1,1)',146, 146, 146, 146, 146, 210],
          ['bdMaze3', '(35, 1)', '(1,1)',74, 74, 74, 74, 74, 210],
          ['bdMaze4', '(33, 19)', '(1,1)',80, 80, 80, 80, 80, 180],
          ['bigMaze', '(35, 1)', '(1,1)',210, 210, 210, 210, 210, 80],
          ['bigMaze1', '(33, 27)', '(1,1)',70, 70, 70, 70, 70, 210],
          ['bigMaze2', '(29, 33)', '(1,1)',68, 68, 68, 68, 68, 82],
          ['bigMaze3', '(18, 27)', '(1,1)',77, 77, 77, 77, 77, 110],
          ['bigMaze4', '(33, 27)', '(1,1)',70, 70, 70, 70, 70, 77],
          ['bigMaze5', '(19, 35)', '(1,1)',76, 76, 76, 76, 76, 74],
          ['bigMaze6', '(8, 1)', '(1,1)',57, 57, 57, 57, 57, 205],
          ['bigMaze7', '(32, 27)', '(1,1)',113, 113, 113, 113, 113, 385],
          ['megaMaze', '(68, 70)', '(1,1)',148, 148, 362, 148, 148, 32]]

print("Path Cost for Custom mazes:")
print(tabulate(table4))

table5 = [['Bidirectional-MM0', 'A*', 'UCS', 'BFS', 'DFS'],
          ['0.005416089', '0.243325182', '0.035988791', '0.035988791', '0.16416527']
          ]

print("P Value Table:")
print(tabulate(table5))

df = pd.DataFrame([['Small Maze', 45, 54, 53, 92, 92, 59],
                   ['Medium Maze',177, 185, 221, 269, 269, 146],
                   ['Big Maze',610, 608, 549, 620, 620, 390],
                   ['Tiny Corners', 205, 210, 199, 252, 252, 51],
                   ['Medium Corners', 797, 818, 1136, 1966, 1966, 371],
                   ['Big Corners', 2668, 2705, 4380, 7949, 7949, 504],
                  ],
                  columns=['Search', 'Bi Directional MM',"Bi Directional MM0", "A*", "UCS", "BFS", "DFS"])

df.plot(x='Search',kind='bar', stacked=False,title='Number of Nodes Expanded', figsize=(10,4), fontsize='large', rot=45)
plt.legend(bbox_to_anchor=(1.0, 1.0))
plt.show()

df = pd.DataFrame([['Small Maze', 19, 19, 19, 19, 19, 49],
                   ['Medium Maze', 68, 68, 68, 68, 68, 130],
                   ['Big Maze', 210, 210, 210, 210, 210, 210],
                   ['Tiny Corners', 33, 33, 28, 28, 28, 47],
                   ['Medium Corners', 106, 106, 106, 106, 106, 221],
                   ['Big Corners', 162, 162, 162, 162, 162, 302],
                  ],
                  columns=['Search', 'Bi Directional MM',"Bi Directional MM0", "A*", "UCS", "BFS", "DFS"])

df.plot(x='Search',kind='bar', stacked=False,title='Path Cost', figsize=(10,4), fontsize='large', rot=45)
plt.legend(bbox_to_anchor=(1.0, 1.0))
plt.show()

df = pd.DataFrame([['bdMaze2', 524, 537, 586, 633, 633, 335],
                   ['bdMaze4', 282, 274, 312, 582, 582, 325],
                   ['bigMaze1', 315, 333, 388, 666, 666, 390],
                   ['bigMaze2', 242, 249, 278, 658, 658, 437],
                   ['bigMaze4', 273, 277, 316, 628, 628, 355],
                   ['megaMaze', 1922, 1934, 1154, 2639, 2639, 2331],
                  ],
                  columns=['Search', 'Bi Directional MM',"Bi Directional MM0", "A*", "UCS", "BFS", "DFS"])

df.plot(x='Search',kind='bar', stacked=False,title='Number of Nodes Expanded', figsize=(10,4), fontsize='large', rot=45)
plt.legend(bbox_to_anchor=(1.0, 1.0))
plt.show()

df = pd.DataFrame([['bdMaze2', 146, 146, 146, 146, 146, 210],
                   ['bdMaze4', 80, 80, 80, 80, 80, 180],
                   ['bigMaze1', 70, 70, 70, 70, 70, 210],
                   ['bigMaze2', 68, 68, 68, 68, 68, 82],
                   ['bigMaze4', 70, 70, 70, 70, 70, 77],
                   ['megaMaze', 148, 148, 362, 148, 148, 32],
                  ],
                  columns=['Search', 'Bi Directional MM',"Bi Directional MM0", "A*", "UCS", "BFS", "DFS"])

df.plot(x='Search',kind='bar', stacked=False,title='Path Cost', figsize=(10,4), fontsize='large', rot=45)
plt.legend(bbox_to_anchor=(1.0, 1.0))
plt.show()