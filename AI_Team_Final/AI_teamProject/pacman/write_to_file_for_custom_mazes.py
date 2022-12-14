import os
from pathlib import Path
result_storage_path = Path.cwd()
extension = "\Results_Custom_Test"
path=str(result_storage_path)+extension
folderMade = os.path.exists(path)

if not folderMade:
   os.makedirs(path)
   print("Results folder created in Local")


for j in ["bdmm,heuristic=manhattanHeuristic", "bdmm0",  "astar,heuristic=manhattanHeuristic", "ucs", "bfs","dfs"]:
    for i in ["bdMaze", "bdMaze1", "bdMaze2", "bdMaze3", "bdMaze4", "bigMaze", "bigMaze1", "bigMaze2", "bigMaze3", "bigMaze4", "bigMaze5", "bigMaze6", "bigMaze7", "testMega"]:
        algo = j.split(',')
        if len(algo) == 2:
            sep_equal = algo[1].split('=')
            fn = j
            text_file_ext = algo[0] + "_" + sep_equal[0] + "_" + sep_equal[1]
        else:
            fn = algo[0]
            text_file_ext = algo[0]
        s="python pacman.py -l "+i+" -z .5 -p SearchAgent -a fn="+fn+" -q>./Results_Custom_Test/output_"+i+"_"+text_file_ext+".txt"
        print(s)
        os.system(s)

read_files = os.listdir(path)
open('Cumulative_Results_Custom_Mazes.txt', 'w').close()
with open("Cumulative_Results_Custom_Mazes.txt", "wb") as out:
    for f in read_files:
        f=path+"\\"+f
        with open(f, "rb") as inp:
            if "_" in f:
                s=f[f.index("_")+1:f.index(".")]+"\n"
                out.write(s.encode())
                out.write(inp.read())
                out.write("\n".encode())