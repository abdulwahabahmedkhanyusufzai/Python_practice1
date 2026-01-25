import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
x = np.linspace(0,5,11)
y = x**2

plt.plot(x,y)
plt.title("Hello")
plt.xlabel("Height")
plt.ylabel("Weight")

plt.subplot(2,2,1)
plt.plot(x,y)
plt.subplot(2,2,4)
plt.plot(x,y)

fig = plt.figure()
axis1 = fig.add_axes([0.1,0.1,1,1])
axis2 = fig.add_axes([0.1,0.1,1,1])
axis2.plot(x,y)

fig1 = plt.figure(figsize=(20,8),dpi=100)
axis1 = fig1.add_axes([0.1,0.1,.4,.4])
axis1.plot(x,y)
axis2 = fig1.add_axes([0.3,0.4,.3,.3])
axis2.plot(x,y)

plt.scatter(x,y)
plt.hist(x)
plt.show()

plt.boxplot(x)
plt.show()

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y)
plt.savefig("basicplot.png")
img = mpimg.imread("basicplot.png")
plt.imshow(img)
print(img)

cropped_img = img[100:200, 100:200]
plt.imshow(cropped_img)

plt.plot(x,color="pink")
plt.show()

xaxis = np.linspace(0,5,11)
fig,ax = plt.subplots(figsize=(12,6))

ax.plot(xaxis,xaxis+1,color="red",linewidth=0.25)
ax.plot(xaxis,xaxis+2,color="red",linewidth=0.50)
ax.plot(xaxis,xaxis+3,color="red",linewidth=1.00)
ax.plot(xaxis,xaxis+4,color="red",linewidth=2.00)


ax.plot(xaxis,xaxis+5,color="green",lw=3,linestyle="-")
ax.plot(xaxis,xaxis+6,color="green",lw=3,linestyle="-.")
ax.plot(xaxis,xaxis+7,color="green",lw=3,linestyle=":")

line, = ax.plot(xaxis,xaxis+8,color="black",lw=1.50)
line.set_dashes([5,50,15,50])


plt.show()