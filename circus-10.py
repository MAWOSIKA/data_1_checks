import random

for i in range(5):
    print(random.randint(1, 53)) 

def lotto_numbers():
    lotto_nums=[]
    for i in range(5):
        lotto_nums.append(random.randint(1, 53))
    return lotto_nums
