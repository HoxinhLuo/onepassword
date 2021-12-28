from random import choice, randint, sample
from onepassword._import import lower, upper, num, symbols


def check_lower_upper(password:str):
    u, l = 0, 0
    for p in password:
        if p.islower():
            l += 1
        if p.isupper():
            u += 1
    return u > 0 and l > 0


def check_digit(password:str):
    c = False
    for p in password:
        if p.isdigit():
            c = True
            break
    return c


def check_symbol(password:str):
    c = False
    for p in password:
        if p in symbols:
            c = True
            break
    return c


def check_password(password, is_number=True, is_symbol=False):

    if not check_lower_upper(password):
        return False

    c = False
    if is_number:
        c = check_digit(password)
    if is_symbol:
        c = check_symbol(password)

    return c


def getrandompassword(
        is_numbers='true', is_symbols='false',
        length=8, _type='characters'):

    if _type == 'pin':
        all_ = num

    elif _type == 'memorable':
        all_ = lower

    else:
        all_ = lower + upper
        if is_numbers == 'true':
            all_ += num
        if is_symbols == 'true':
            all_ += symbols

    if _type in ['pin', 'characters']:
        password = ''.join([choice(all_) for _ in range(length)])
    else:
        p = []
        for _ in range(length):
            pp = sample(all_, k=randint(4, 8))
            pp = ''.join(pp)
            p.append(pp)
        password = '-'.join(p)

    if _type == 'characters':
        while not check_password(password):
            password = ''.join([choice(all_) for _ in range(length)])

    return password
