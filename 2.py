import random

def turtle(pos_t):
    t = random.randint(1, 11)
    if t < 6:
        pos_t += 3
    elif t < 8:
        pos_t -= 5
        if pos_t <= 0:
            pos_t = 1
    else:
        pos_t += 1
    return pos_t


def hare(pos_h):
    h = random.randint(1, 11)
    if h < 3:
        pos_h += 0
    elif h < 5:
        pos_h += 7
    elif h < 6:
        pos_h -= 10
        if pos_h <= 0:
            pos_h = 1
    elif h < 9:
        pos_h += 1
    else:
        pos_h -= 2
        if pos_h <= 0:
            pos_h = 1
    return pos_h

def race():
    pt = 0
    ph = 0
    time = 0
    print("ON YOUR MARK... GET SET...")
    print("GO!!!!!")
    print("AND THEY'RE OFF!")
    print('')
    for time in range(50):
        pt += turtle(pt)
        ph += hare(ph)
        lists = " " * 50
        race_track = list(lists)
        time += 1

race()