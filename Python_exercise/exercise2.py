'''
Sum all even numbers in a list called "nums" Return -1 if no valid even numbers are found

'''
def sum_even_nums(nums):
    sum_even_nums = 0
    lista= []
    for num in nums:
        if type(num) == int or type(num) == float:
            if num % 2 == 0:
                lista.append(num)
            else: 
                continue
        else:
            continue
        
    if len(lista) == 0:    
        sum_even_nums = -1
        
    else:
        sum_even_nums = sum(lista)
        
    return sum_even_nums

print(sum_even_nums([2,3,4]))
print(sum_even_nums([2,3,-4]))
print(sum_even_nums([]))
print(sum_even_nums([0.2,4,-7]))
print(sum_even_nums([[6,4,2],4,-8]))
