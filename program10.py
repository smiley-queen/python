"""from functools import cmp_to_key
@cmp_to_key
def custom_compare(a,b):
    value1=str(a)+str(b)
    value2=str(b)+str(a)
    if value1<value2:
        return 1
    elif value1>value2:
        return -1
    else:
        return 0
def findLargestNumber(numbers):
    numbers.sort(key=custom_compare)
    return ''.join(map(str,numbers))
numbers=[10,68,97,9,21,12]
largestNumber=findLargestNumber(numbers)
print('the largest number is',largestNumber)
"""
def find_largest_number(numbers):
    numbers_as__strings=list(map(str,numbers))
    numbers_as__strings.sort(reverse=True)
    result= ''.join(numbers_as__strings)
    return int(result)if '.' not in result else float(result)
integer_numbers=[93,68,721,6]
largest_integer=find_largest_number(integer_numbers)
print("largest integer:",largest_integer)