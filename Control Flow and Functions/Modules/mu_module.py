my_fav_num=3.14
# module:spliting the functionity differently
# a module is a file containing python definations and statements
# import used for modules
# The defining characteristic of a traditional package is the presence of an
# __init__.py file within its directory.
'''
my_project/    package
├── main.py   module(with extenstions)
└── data_analysis/  package
    ├── __init__.py
    ├── cleaning.py
    └── visualization.py
    └── models/  package
        ├── __init__.py
        └── regression.py

import data_analysis.cleaning # Imports the cleaning module from the data_analysis package
from data_analysis import visualization # Imports the visualization module directly
from data_analysis.models import regression # Imports the regression module from the models subpackage
'''