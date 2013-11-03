import os

os.chdir('/home/msl/Documents/programming/python/head_first_python/chapter3')
file = open('data.txt')
for line in file:
    (planet, moons) = line.split(':')
    moons = moons.split(',')
    moonString = ''
    while moons.next():
        moonString += moon + ', '
    moonString += moons.last()
    print('planet: ' + planet + '\t\tmoons: ' + moonString, end = '')

file.close()
