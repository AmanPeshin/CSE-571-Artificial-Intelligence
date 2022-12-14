import os
from pathlib import Path
result_storage_path = Path.cwd()
extension = "\Results_Default_Test"
path=str(result_storage_path)+extension
folderMade = os.path.exists(path)

if not folderMade:
   os.makedirs(path)
   print("Results folder created in Local")


for j in ["bdmm,heuristic=manhattanHeuristic", "bdmm0",  "astar,heuristic=manhattanHeuristic", "ucs", "bfs","dfs"]:
    for i in ["smallMaze", "mediumMaze", "bigMaze", "tinyCorners", "mediumCorners", "bigCorners"]:
        algo = j.split(',')

        if len(algo) == 2:
            temp = algo[1]
            sep_equal = temp.split('=')
            fn = j
            text_file_ext = algo[0]+"_"+sep_equal[0]+"_"+sep_equal[1]
        else:
            fn = algo[0]
            text_file_ext = algo[0]

        if i == "tinyCorners" or i == "mediumCorners" or i == "bigCorners":
            if len(algo) == 2:
                if j == "astar,heuristic=manhattanHeuristic":
                    algo[0] = "aStarSearch"
                s="python pacman.py -l "+i+" -p SearchAgent -a fn="+algo[0]+",prob=CornersProblem,heuristic=cornersHeuristic -q >./Results_Default_Test/output_"+i+"_"+text_file_ext+".txt"
            else:
                s="python pacman.py -l "+i+" -p SearchAgent -a fn="+algo[0]+",prob=CornersProblem -q >./Results_Default_Test/output_"+i+"_"+text_file_ext+".txt"
        else:
            s="python pacman.py -l "+i+" -z .5 -p SearchAgent -a fn="+fn+" -q >./Results_Default_Test/output_"+i+"_"+text_file_ext+".txt"
        print(s)
        os.system(s)

read_files = os.listdir(path)
open('Cumulative_Results_Default_Mazes.txt', 'w').close()
with open("Cumulative_Results_Default_Mazes.txt", "wb") as out:
    for f in read_files:
        f=path+"\\"+f
        with open(f, "rb") as inp:
            if "_" in f:
                s=f[f.index("_")+1:f.index(".")]+"\n"
                out.write(s.encode())
                out.write(inp.read())
                out.write("\n".encode())