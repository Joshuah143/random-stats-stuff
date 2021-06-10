import random


def ecalc(length=100000):
    e = 1
    count = 1
    den = 1
    for i in range(length):
        e += 1/den
        count += 1
        den = count * den
    print(e)
    return e


def montyhall(calcs=50000):
    wrightnochange = 0
    wrightchange = 0
    for i in range(calcs):
        car = random.randint(0, 2)
        choice = random.randint(0, 2)
        if choice == car:
            wrightnochange += 1
        else:
            continue
    for i in range(calcs):
        car = random.randint(0, 2)
        choice = random.randint(0, 2)
        reveal = random.randint(0, 2)
        while choice == reveal or reveal == car:
            reveal = random.randint(0, 2)
        for t in range(2):
            if t != reveal and t != choice:
                wrightchange += 1
    print(f'no change: {wrightnochange} out of {calcs}, thats {round((wrightnochange/calcs), 3) * 100}%')
    print(f'change: {wrightchange} out of {calcs}, thats {round((wrightchange / calcs), 3) * 100}%')


def sqrt(num, accuraccy=0.00005, lessthanone=False, largenumber=False):
    if num > 210 and not largenumber:
        print('thats too big of a number, i can round it up for you if you like, you just need to spicy in the keyword arguments')
        return 'Error, too big'
    if not lessthanone:
        sqt = findlow(lowerbound=1, increment=1, number=num)
    else:
        sqt = findlow(lowerbound=0, increment=0.0001, number=num)
    while (sqt[1] - sqt[0]) >= accuraccy:
        inc = ((sqt[1] - sqt[0]) / 100)
        sqt = findlow(lowerbound=sqt[0], increment=inc, number=num)
    return [sqt[0], sqt[1]]


def ycalc(x, num):
    ret = float((num / x) + x)
    return ret


def findlow(lowerbound, increment, number):
    x = lowerbound
    while ycalc(x, number) > ycalc(x + increment, number):
        x += increment
    return [x, x + increment]





