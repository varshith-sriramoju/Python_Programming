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