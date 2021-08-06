def max_101(num1,num2):
    if num1 > num2:
        return num1
    elif num1< num2:
        return num2
    else:
        return "Equal"

def max_of_three(x,y,z):
    if x >= z and x >= y:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

    #assuming you're not testing with 2 equal inputs

def rental_late_fee(days):
    if days <= 0:
        return 0
    elif days <= 9 and days > 0:
        return 5
    elif days <= 15 and days > 9:
        return 7
    elif days <= 24 and days > 15:
        return 19
    else:
        return 100





