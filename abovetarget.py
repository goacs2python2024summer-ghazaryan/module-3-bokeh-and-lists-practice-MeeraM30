argument1 = input("Please input your list of values, seperated by a comma. \n")
x = list(map(float, argument1.split(",")))

argument2 = input("Now input your target value. \n")
target = float(argument2)


def aboveTarget(myList, target):
    for item in myList:
        if item > target:
            return True
        
    return False

print(aboveTarget(x,target))