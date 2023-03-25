def snow_ball(max_number):

    sum = 0 

    for number in range(1, max_number +1):
        sum += number

    return sum

my_result=snow_ball(100)
print(my_result)