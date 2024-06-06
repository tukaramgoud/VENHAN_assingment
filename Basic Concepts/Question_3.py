"""3. Given a list of integers, write a function `sum_of_squares(lst: List[int]) -> int` that
returns the sum of the squares of the elements."""

numbers_list = [1,2,3,4,5]

def map_sum(n):
    return n+n

def sum_of_squares(list_is):

    print(sum(list_is))  #by using inbuild sum function we can easily find out sum

    
    new_sum = 0
    for i in list_is:     # or we can use loops for finding sum 
        new_sum += i
    print(new_sum)

sum_of_squares(numbers_list)