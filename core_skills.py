import random
rand_list = random.sample(range(1,21), 10)
# print(rand_list)

list_comprehension_below_10 = [rand for rand in rand_list if rand <10]
# print(list_comprehension_below_10)

list_comprehension_below_10 = list(filter(lambda x: x<10, rand_list))
# print(list_comprehension_below_10)