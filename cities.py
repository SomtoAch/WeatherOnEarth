import csv
import random

num_lines = 47870

def getThreeCities():
    csv_file = open('worldcities.csv', encoding='utf-8')
    csv_reader = csv.reader(csv_file)

    rand1 = random.randint(0, num_lines)
    rand2 = random.randint(0, num_lines)
    rand3 = random.randint(0, num_lines)

    c = 0

    city1=[]
    city2=[]
    city3=[]

    for line in csv_reader:
        if c == rand1:
            city1 = [line[0], line[2], line[3], line[4]]
            c+=1
        elif c == rand2:
            city2 = [line[0], line[2], line[3], line[4]]
            c+=1
        elif c == rand3:
            city3 = [line[0], line[2], line[3], line[4]]
            c+=1
        else:
            c+=1

    return [city1, city2, city3]
        