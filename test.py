'''
import csv

with open("weather.csv", 'r') as file:
    data = list(csv.reader(file))

print(data)

city = input("Enter a city:")

for row in data: 
    if row[0] == city:
        print(row[1])


import glob

myfiles = glob.glob("p/*.txt")
print(myfiles)

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())

def get_average(): 
    with open("data.txt","r") as file: 
        temp = file.readlines()
        values = temp[1:]
        values = [float(i) for i in values]
        average_local = sum(values) / len(values)

    return average_local

avg = get_average()
print(avg)

def get_max_min():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    print(f'Max:{maximum}, Min:{minimum}')
    return maximum, minimum
   
    
max_min = get_max_min()
print(max_min)




def calculate_time(h,g=9.80665):
    t = (2 * h / g) ** 0.5
    return t
    
time = calculate_time(100)
print(time)

freezing_point = 0
boiling_point = 100

def water_state(temperature):
    if temperature <= freezing_point:
        return "Solid"
    elif 0 < temperature < boiling_point:
        return "Liquid"
    else:
        return "Gas" '''
    
import random

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

print(random.randrange(lower,upper))



