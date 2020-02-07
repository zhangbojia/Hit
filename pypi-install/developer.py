import turtle
import random
def r(w,rangestart,rangeend):
    """\'w\' means Way -> str
    r will output as float betwenn rangestart and rangeend
    ri will output as int betwenn rangestart and rangeend
    """
    if w == 'r':
        print(random.random(rangestart , rangeend))
    if w == 'ri':
        print(random.randint(rangestart,rangeend))
r('ri', 100 , 500)