def csSumOfPositive(input_arr):
    if len(input_arr) == 0:
        return 0
    result = 0
    for num in input_arr:
        if num > 0:
            result += num
    return result
    

