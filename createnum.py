import random

def generator_number():
    """Возврощает сгнерированное четырехзначное число
    """
    x = ''.join(random.sample('0123456789', 4))
    if x[0] == '0':
        return generator_number()
    return x

def check_enter_number(x):
    """Проверяет введеное число на корректность
    """
    if not x.isdigit() or not len(x) == 4:
        return False
    for i in range(0, len(x)):
        if i != x.find(x[i]):
            return False
    return True
