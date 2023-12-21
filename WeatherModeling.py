import pandas as pd
import numpy as n
import matplotlib.pyplot as p
l=[] 
def quadratic_solver(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        return None 
    else:
        root1 = (-b + n.sqrt(D)) / (2*a)
        root2 = (-b - n.sqrt(D)) / (2*a)
        return root1, root2
    
def weather_model(a, b, c):
    roots = quadratic_solver(a, b, c)
    l.append(roots[0])
    if roots:
        temperature = roots[0] 
        return f"The predicted temperature is: {temperature} degrees Celsius"
    else:
        return "No real solutions, check your input coefficients."
    

print('Stage 1: Hard-coding variables')
a = 1
b = -3
c = 2
print(weather_model(a, b, c))
print('\n')

print('Stage 2: Keyboard input')
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: ")) 
c = float(input("Enter coefficient c: "))
print(weather_model(a, b, c))
print('\n')

print('stage 3: read from a file using pandas')
file_path = 'wea2.csv'
df = pd.read_csv(file_path)
for index, row in df.iterrows():
    x,y,z = row['a'], row['b'], row['c']
print(weather_model(x,y,z))
print()

print('Stage 4: Read from a file multiple set of data using pandas')
file_path = 'wea.csv'
df = pd.read_csv(file_path)
for index, row in df.iterrows():
    x,y,z = row['a'], row['b'], row['c']
    result = weather_model(x,y,z)
    print(f"For set {index + 1}: {result}")

p.plot(l,marker='x', linestyle='dashed', color='g')
p.title('Roots')
p.xlabel('Time')
p.ylabel('Temp')
p.legend(title="Temperature")
p.show()
