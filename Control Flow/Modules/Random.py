#module:spliting the functionity differently
#a module is a file containing python definations and statements
#import used for modules
#The defining characteristic of a traditional package is the presence of an
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
import random
import random as r
import mu_module
num=r.randint(1,10)
print("random number:"+str(num))
print(mu_module.my_fav_num)

#recommended
ran_num=random.random() #0.0000000000 to 1.0
print(ran_num)
ran_num=random.random()*100 #0.0000000000 to 1.0
print(ran_num)

ran_float=random.uniform(1,10)
print(ran_float)

#heads or tails
head_tails=random.randint(0,1)
if head_tails==1:
    print("heads")
else:
    print("tails")