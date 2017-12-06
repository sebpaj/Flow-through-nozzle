import matplotlib.pyplot as plt

x = []
y = []
j = 1

fo = open('velProfile.txt','r')       #import data from file
var = fo.read()
print(var)
var = var.split()


for i in var:
    if j%2 != 0:
        x.append(i)
    if j%2 == 0:
        y.append(i)
    j += 1
    
plt.plot(x,y)               #plot velocity profile