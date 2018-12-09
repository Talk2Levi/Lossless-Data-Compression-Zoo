import math
import random


def mtf_random(input_file):

    ascii_list = []
    access_cost_list = []

    for i in range(0,128):
        ascii_list.append(i)

    seed = 1
    random.seed(seed)

    with open("./"+input_file+".txt") as f:
        while True:
            c = f.read(1)
            if not c:
                break

            if ord(c) < 128:
                # find the index of that char
                index = ascii_list.index(ord(c))
                # record the access cost
                access_cost_list.append(index)
                # randomly move to front by x index
                x = random.randint(0, index)
                ascii_list.pop(index)
                ascii_list.insert(x, ord(c))

    j=0       
    cost = 0
    cost_number = 0

    while j < len(access_cost_list):
        cost += 2*math.floor( math.log(access_cost_list[j]+1, 2) ) +1
        cost_number += access_cost_list[j]
        j += 1

    print ("the cost is: ", cost, " bits ", cost/8, " bytes", " compression ration is ", cost/8/len(access_cost_list))

input_file = "bib"
mtf_random(input_file)