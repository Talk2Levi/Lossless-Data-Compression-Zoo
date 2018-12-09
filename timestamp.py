import math

class Timestamp:
    

    def __init__(self):
        self.access_cost_list = []

    def timestamp(self, input_file):
        asciiList = []
        stampList = []
        cost = 0
        for i in range(0,127):
            asciiList.append(i)
            stampList.append([])

        with open("./"+input_file+".txt") as f:
            while True:
                c = f.read(1)
                if not c:
                    break

                if ord(c) < 128:
                    self.access_cost_list.append(asciiList.index(ord(c)))
                    stampList[ord(c)].append(ord(c))
                    self.checkMove(asciiList, stampList[ord(c)], ord(c))
                    for l in stampList:
                        if not len(l) == 0 and not stampList.index(l) == c:
                            l.append(c)
        
        j=0
        cost = 0
        cost_number = 0
        
        while j < len(self.access_cost_list):
            cost += 2*math.floor( math.log(self.access_cost_list[j]+1, 2) ) +1
            cost_number += self.access_cost_list[j]
            j += 1

        print ("the cost is: ", cost, " bits ", cost/8, " bytes", " compression ration is ", cost/8/len(self.access_cost_list))                
                
    def checkMove(self, asciiList, l, c):
        if l.count(c) > 1:
            for i in range(0, 127):
                if l.count(asciiList[i]) <= 1:
                    asciiList.pop(asciiList.index(c))
                    asciiList.insert(i, c)
                    break
            l = [c]

# main
input_file = "bib"
time_step_compression = Timestamp()
time_step_compression.timestamp(input_file)
