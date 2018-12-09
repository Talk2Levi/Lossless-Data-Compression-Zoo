import math

# Compression Step
def mtf(input_file):

    asciiList = []
    access_cost_list = []

    for i in range(0,128):
        asciiList.append(i)

    with open("./"+input_file+".txt") as f:
        while True:

            c = f.read(1)
            if not c:
                break

            if ord(c) <= 127:
                index = asciiList.index(ord(c))
                # record the access cost
                access_cost_list.append(index)
                # remove that char from the list
                asciiList.pop(index)
                # insert that char at the front of the list
                asciiList.insert(0, ord(c))
            
    j=0
    cost = 0
    cost_number = 0
    while j < len(access_cost_list):
        cost += 2*math.floor( math.log(access_cost_list[j]+1, 2) ) +1
        cost_number += access_cost_list[j]
        j += 1


    print("the cost is: ", cost, " bits ", cost/8, " bytes", " compression ration is ", cost/8/len(access_cost_list))
    print("number is: ", cost_number)

# Decompression Step
def mtf_reverse(access_cost_list):
    asciiList = []
    with open("testOutput.txt", 'w') as file_handler:
        for i in range(0,128):
            asciiList.append(i)
        for j in access_cost_list:
            # find the value of that item in cost list, that is the char we reverted
            value = asciiList[j]
            # find the index
            index = asciiList.index(value)
            # write that char in file
            file_handler.write(chr(value))
            # remove the index
            asciiList.pop(index)
            # insert at the front
            asciiList.insert(0, value)

def writeList(access_cost_list):
    with open("cost.txt", 'w') as file_handler:
        for j in access_cost_list:
            file_handler.write(" "+str(j))

def checkChars():
    with open("../dataset_after_bwt/alice29.txt") as f:
        while True:
            c = f.read(1)
            if not c:
                print("End of file")
                break
            if ord(c)>126 and ord(c)<32:
                print("error")


input_file = "bib"
mtf(input_file)