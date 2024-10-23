import random
# import my_module
# print(my_module.my_fav_number))
rand_num = random.randint(1, 10)
print(rand_num)


# ran_num_0_to_1=random.random
ran_num_0_to_1=random.random()*10 #we can multiply so it can generate number from 0 to 10

print(ran_num_0_to_1)


# Heads or Tails
coin=random.randint(0,1)
if coin==1:
    print("Heads")
elif coin==0:
    print("Tails")