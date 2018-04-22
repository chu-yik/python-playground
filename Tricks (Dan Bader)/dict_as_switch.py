# There is no switch case in python
# so we have two options - 
# 1. using nested if-elif
# 2. using dict as switch case
# this utilise the fact that functions are
# first-class members in python

def switch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None

def switch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

print(switch_if('mul', 2, 8))
print(switch_if('unknown', 2, 8))

print(switch_dict('mul', 2, 8))
print(switch_dict('unknown', 2, 8))
