#Kadari Faulkner
#12/11/2021
# Problem 3 for multiply all the numbers in the list

def multiplylist(alist):
    total = 1
    for num in alist:
        total = num * total
    return total

my_list = [5, 2, 7, -1]
print("the total is:", multiplylist(my_list))