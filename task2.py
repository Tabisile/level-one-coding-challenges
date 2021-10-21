def contains_a_three(a,b):
    sum_as_int = int(a+b)
    sum_as_string = str(sum_as_int)
    sum_contains_3 = '3' in sum_as_string
    if(a == 3 or b == 3) and (sum_contains_3 == True):
       return True
    else:
       return False
