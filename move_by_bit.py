import math

def mbb(input_file):

    ascii_list = []
    ascii_bit_list = []
    access_cost_list = []

    for i in range(0,128):
        ascii_list.append(i)
        ascii_bit_list.append(0)

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

                if(ascii_bit_list[index] == 0):
                    # Flip the bit to 1 and move the next time
                    ascii_bit_list[index] = 1
                else:
                    # remove that char from the list
                    ascii_list.pop(index)
                    # insert that char at the front of the list
                    ascii_list.insert(0, ord(c))
                    # flip the bit back to zero
                    ascii_bit_list[index] = 0
                    ascii_bit_list.pop(index)
                    ascii_bit_list.insert(0, 0)

    j=0       
    cost = 0
    cost_number = 0

    while j < len(access_cost_list):
        cost += 2*math.floor( math.log(access_cost_list[j]+1, 2) ) +1
        cost_number += access_cost_list[j]
        j += 1
    print ("the cost is: ", cost, " bits ", cost/8, " bytes", " compression ration is ", cost/8/len(access_cost_list))
    print ("%2.7g" %(cost/8/len(access_cost_list) * 100))

# main
input_file = "bib"
mbb(input_file)