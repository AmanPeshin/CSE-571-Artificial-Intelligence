set "python=C:\Users\Aman-ASU\My Graduate\Artificial Intelligence\Projects\cse571.1\Scripts\python.exe"
set "pip=C:\Users\Aman-ASU\My Graduate\Artificial Intelligence\Projects\cse571.1\Scripts\pip.exe"
"%pip%" install numpy %*
"%pip%" install pathlib %*
"%pip%" install matplotlib %*
"%pip%" install pandas %*
"%pip%" install tabulate %*
"%python%" write_to_file_for_default_mazes.py %*
"%python%" write_to_file_for_custom_mazes.py %*
"%python%" generate_graphs.py %*
pause