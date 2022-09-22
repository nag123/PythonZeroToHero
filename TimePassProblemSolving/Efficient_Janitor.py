import itertools

'''
2.5 1.4 1.01 1.01 1.01
templist = [2.5]
'''
def efficientJanitor(weight):
    # Write your code here
    sortedvalueofweight = sorted(weight,key=float,reverse=True)
    temp = []
    counter = 0
    total = 0
    for i in range(0,len(sortedvalueofweight)+1):
        total = sum(temp)
        if ((i == len(sortedvalueofweight)) and (len(temp) > 0)):
            counter = counter + 1
        if(i == len(sortedvalueofweight)):
            if(total >= 3):
                counter = counter + 1
        else:
            if(total <=3):
                temp.append(sortedvalueofweight[i])
            else:
                temp.clear()
                temp.append(sortedvalueofweight[i-1])
                temp.append(sortedvalueofweight[i])
                counter = counter +1
    return counter

if __name__ == '__main__':
    weight_count = int(input().strip())
    weight = []

    for _ in range(weight_count):
        weight_item = float(input().strip())
        weight.append(weight_item)

    result = efficientJanitor(weight)
    print(result)
