Bi-Directional Search 
All Instructions are given for Windows Machine.

Method 1: Windows Batch File

How to run our test cases: 

1. Open Batch file "script_to_run_project" inside Pacman folder
2. On line 1, enter the path to your python.exe file of your virtual environment
   On line 2, enter the path to your pip.exe file of your virtual environment
3. save and close editor window
4. Double click on the batch file to run different test scenario (The inbuilt mazes or custom mazes, this would also generate all the tables in the report and the vizualizations)
5. You will see a folder created called "Results_Default_Cases" and "Results_Custom_Cases"
6. You can view individual txt file outputs for individual mazes run respectively inside these folder.
7. Also, you can view the compiled txt file containing all outputs as "Cumulative_Results_Default_Mazes" and "Cumulative_Results_Custom_Mazes" in the main Pacman directory

Method 2: Run individual python files

How to run our test cases: 
1. pip install pathlib, in your virtual environment
2. Run the python script "write_to_file_for_default_mazes" and "write_to_file_for_custom_mazes"
3. You will see a folder created called "Results_Default_Cases" and "Results_Custom_Cases"
4. You can view individual txt file outputs for individual mazes run respectively inside these folder.
5. Also, you can view the compiled txt file containing all outputs as "Cumulative_Results_Default_Mazes" and "Cumulative_Results_Custom_Mazes" in the main Pacman directory

How to generated charts and tables present in the report:
1. pip install numpy, pandas, matplotlib, tabulate in your virtual environment
2. run the python script generate_graphs.py
3. The four charts and 5 tables used in report will be displayed in a dialog box.

Results such as Nodes expanded and Path cost are tabulated from the above test cases and statistical analysis done in the report.
