#kadari Faulkner
#12/11/2021
#problem 4 taking a list of numbers and returns a new one

def random(alist):
    random_list = []
    for num in alist:
        if num not in random_list:
            random_list.append(num)
        return random_list

print(random([1, 3, 3, 3, 6, 2, 3, 5, 120, 150]))
