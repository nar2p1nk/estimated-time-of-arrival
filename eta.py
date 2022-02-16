def distance(time,speed):
    distance = time * speed
    return distance

def speed(distance,time):
    speed = distance / time
    return speed

def time(distance,speed):
    time = distance / speed
    return time

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('distance', help='insert distance')

parser.add_argument('speed',help='insert speed')

parser.add_argument('time',help='insert time')
