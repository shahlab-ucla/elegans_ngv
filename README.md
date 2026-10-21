These files contain all necessary information for replicating all figures within the paper. 
Certain portions of the code have been separated into their own files due to memory constraints and length of runtime.

To generate the volumes:
- run Volume_calculations.py with the corresponding coordinates.pickle and names.pickle files.

To generate the p values from permutation analysis:
- run Permutation_Calculator.py with the corresponding fulldictlist.pkl.

To generate the main figures:
- run the two above preqrequisite scripts within the same directory that you plan to run Main_Figures.ipynb.
- the file outputs from those scripts will run within this Jupyter Notebook to produce all figures. 
