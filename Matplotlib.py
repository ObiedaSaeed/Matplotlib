#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Graph Styling
# https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
plt.style.use('seaborn-darkgrid')


# In[3]:


# By default Plot() function will draw a line chart.
x = np.array([1,2,3,4,5,6])
y = np.power(x,3)
plt.plot(x,y)
plt.show()


# In[4]:


x = np.linspace(0, 10, 1000)
y = np.sin(x) # Sine Graph
plt.plot(x,y)
plt.show()


# In[5]:


# Recover default matplotlib settings
mpl.rcParams.update(mpl.rcParamsDefault)


# In[6]:


x = np.linspace(0, 10, 1000)
y = np.sin(x) # Sine Graph
plt.plot(x,y)
plt.show()


# In[7]:


plt.style.use('seaborn-darkgrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


# Solid red line will be plotted using the argument "r-"
plt.figure(figsize=(10,5))
x = np.linspace(0, 10, 1000)
y = np.sin(x) # Sine Graph
plt.plot(x,y,'r-')
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.show()


# In[10]:


# Plotting traingular dots using the argument "rv"
plt.figure(figsize=(10,5))
x = np.linspace(0, 10, 40)
y = np.sin(x) # Sine Graph
plt.plot(x,y,'rv')
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.show()


# In[11]:


#Plotting multiple sets of data
plt.figure(figsize=(10,5))
x = np.array([1,2,3,4,5,6])
y1 = np.power(x,2)
y2 = np.power(x,3)
plt.plot(x,y1, "b-" , label = '$y1 = x^2$') # Setting up legends
plt.plot(x,y2, "r-" ,label ='$y2 = x^3$') # Setting up legends
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.legend()
plt.tight_layout()
plt.show()


# In[12]:


# Line Styling
x = np.linspace(0, 10, 2000)
plt.figure(figsize=(16, 9))
plt.plot(x,np.sin(x) , label = '$Sin(X) $ $ Dashed $' , linestyle='dashed')
plt.plot(x+1,np.sin(x) , label = '$Sin(X) $ $ Dashdot $' , linestyle='dashdot')
plt.plot(x,np.cos(x) , label = '$cos(X) $ $ Solid $' , linestyle='solid')
plt.plot(x+1,np.cos(x) , label = '$cos(X)$ $ Dotted $' , linestyle='dotted')
plt.xlabel(r'$X$' , fontsize = 18)
plt.ylabel(r'$Y$' , fontsize = 18)
plt.title("$Sin(x) $ $ & $ $ Cos(x)$" ,fontsize = 14)
plt.legend(loc = 'upper right' , fontsize = 14 , bbox_to_anchor=(1.2, 1.0)) # Legend will b
plt.show()


# In[13]:


# Shading Regions with fill_between() function
x = np.linspace(0, 10, 2000)
plt.figure(figsize=(10,6))
plt.plot(x,np.sin(x) , label = '$Sin(X)$')
plt.plot(x,np.cos(x) , label = '$cos(X)$')
plt.fill_between(x,0,np.sin(x))
plt.fill_between(x,0,np.cos(x))
plt.xlabel(r'$X$' , fontsize = 18)
plt.ylabel(r'$Y$' , fontsize = 18)
plt.title("$Sin(x) $ $ & $ $ Cos(x)$" ,fontsize = 14)
plt.legend(loc = 'lower left') # Legend will be placed at lower left position
plt.show()


# In[14]:


# Display multiple plots in one figure (2 row & 1 columns)
plt.figure(figsize=(12,6))
x = np.linspace(0, 10, 100)
y1 = np.sin(x) # Sine Graph
y2 = np.cos(x) # cosine graph
plt.subplot(2,1,1)
plt.plot(x,y1, "b-")
plt.subplot(2,1,2)
plt.plot(x,y2, "r-")
plt.tight_layout()
plt.show()


# In[15]:


# # Display multiple plots in one figure using subplots()
x = np.arange(-50,50)
y1 = np.power(x,2)
y2 = np.power(x,3)
y3 = np.sin(x)
y4 = np.cos(x)
y5 = np.tan(x)
y6 = np.tanh(x)
y7 = np.sinh(x)
y8 = np.cosh(x)
y9 = np.exp(x)
fig1 , ax1 = plt.subplots(nrows=3,ncols=3 , figsize = (20,20)) # Create a figure and subplo
ax1[0,0].plot(x,y1,"tab:blue") # set the color of the line chart
ax1[0,0].set_title("Square Function") # setting title of subplot
ax1[0,0].set_xlabel(r'$X$' , fontsize = 18) #Set the label for the x-axis
ax1[0,0].set_ylabel(r'$Y$' , fontsize = 18) #Set the label for the y-axis
ax1[0,1].plot(x,y2,"tab:orange")
ax1[0,1].set_title("Cubic Function")
ax1[0,1].set_xlabel(r'$X$' , fontsize = 18)
ax1[0,1].set_ylabel(r'$Y$' , fontsize = 18)
ax1[0,2].plot(x,y3,"tab:green")
ax1[0,2].set_title("Sine Function")
ax1[0,2].set_xlabel(r'$X$' , fontsize = 18)
ax1[0,2].set_ylabel(r'$Y$' , fontsize = 18)
ax1[1,0].plot(x,y4,"b-")
ax1[1,0].set_title("Cosine Function")
ax1[1,0].set_xlabel(r'$X$' , fontsize = 18)
ax1[1,0].set_ylabel(r'$Y$' , fontsize = 18)
ax1[1,1].plot(x,y5,"r-")
ax1[1,1].set_title("Tangent Function")
ax1[1,1].set_xlabel(r'$X$' , fontsize = 18)
ax1[1,1].set_ylabel(r'$Y$' , fontsize = 18)
ax1[1,2].plot(x,y6,"g-")
ax1[1,2].set_title("Hyperbolic Tangent")
ax1[1,2].set_xlabel(r'$X$' , fontsize = 18)
ax1[1,2].set_ylabel(r'$Y$' , fontsize = 18)
ax1[2,0].plot(x,y7,"m-")
ax1[2,0].set_title("Hyperbolic Sine")
ax1[2,0].set_xlabel(r'$X$' , fontsize = 18)
ax1[2,0].set_ylabel(r'$Y$' , fontsize = 18)
ax1[2,1].plot(x,y8,"y-")
ax1[2,1].set_title("Hyperbolic Cosine")
ax1[2,1].set_xlabel(r'$X$' , fontsize = 18)
ax1[2,1].set_ylabel(r'$Y$' , fontsize = 18)
ax1[2,2].plot(x,y9,"k-")
ax1[2,2].set_title("Exponential Function")
ax1[2,2].set_xlabel(r'$X$' , fontsize = 18)
ax1[2,2].set_ylabel(r'$Y$' , fontsize = 18)
plt.show()


# In[16]:


id1 = np.arange(1,10)
score = np.arange(20,110,10)
plt.figure(figsize=(8,5)) # Setting the figure size
ax = plt.axes()
ax.set_facecolor("#ECF0F1") # Setting the background color by specifying the HEX Code
plt.bar(id1,score,color = '#FFA726')
plt.xlabel(r'$Student $ $ ID$')
plt.ylabel(r'$Score$')
plt.show()


# In[17]:


#Plotting multiple sets of data
x1= [1,3,5,7]
x2=[2,4,6,8]
y1 = [7,7,7,7]
y2= [17,18,29,40]
plt.figure(figsize=(8,6))
ax = plt.axes()
ax.set_facecolor("white")
plt.bar(x1,y1,label = "First",color = '#42B300') # First set of data
plt.bar(x2,y2,label = "Second",color = '#94E413') # Second set of data
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.title ('$Bar $ $ Chart$')
plt.legend()
plt.show()


# In[18]:


# Horizontal Bar Chart
Age = [28,33,43,45,57]
Name = ["Asif", "Steve", 'John', "Ravi", "Basit"]
plt.barh(Name,Age, color ="yellowgreen")
plt.show()


# In[19]:


# Changing the width of Bars
num1 = np.array([1,3,5,7,9])
num2 = np.array([2,4,6,8,10])
plt.figure(figsize=(8,4))
plt.bar(num1, num1**2, width=0.2 , color = '#FF6F00')
plt.bar(num2, num2**2, width=0.2 , color = '#FFB300')
plt.plot()


# In[22]:


plt.style.use('seaborn-darkgrid')
x1= ['Asif','Basit','Ravi','Minil']
y1= [17,18,29,40]
y2 = [20,21,22,23]
plt.figure(figsize=(5,7))
plt.bar(x1,y1,label = "Open Tickets",width = 0.5,color = '#FF6F00')
plt.bar(x1,y2,label = "Closed Tickets",width = 0.5 ,bottom = y1 , color = '#FFB300')
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.title ('$Bar $ $ Chart$')
plt.legend()
plt.show()


# In[27]:


x1 = np.array([250,150,350,252,450,550,455,358,158,355])
y1 =np.array([40,50,80, 90, 100,50,60,88,54,45])
x2 = np.array([200,100,300,220,400,500,450,380,180,350])
y2 = np.array([400,500,800, 900, 1000,500,600,808,504,405])
#Graph - 1
plt.scatter(x1,y1)
plt.xlabel('$Time $ $ Spent$' , fontsize = 12)
plt.ylabel('$Score$' , fontsize = 12)
plt.title ('Scatter Graph')
plt.show()
#Graph - 2
plt.scatter(x2,y2 ,color = 'r')
plt.xlabel('$Time $ $ Spent$' , fontsize = 12)
plt.ylabel('$Score$' , fontsize = 12)
plt.title ('Scatter Graph')
plt.show()
#Graph - 3
plt.scatter(x1,y1 ,label = 'Class 1')
plt.scatter(x2,y2 ,label = 'Class 2',color ='r')
plt.xlabel('$Time $ $ Spent$' , fontsize = 12)
plt.ylabel('$Score$' , fontsize = 12)
plt.title ('Scatter Graph')
plt.legend()
plt.show()
#Graph - 4
plt.scatter(x1,y1 ,label = 'Class 1',marker='o' , color = 'm')
plt.scatter(x2,y2 ,label = 'Class 2',marker='v',color ='r')
plt.xlabel('$Time $ $ Spent$' , fontsize = 12)
plt.ylabel('$Score$' , fontsize = 12)
plt.title ('Scatter Graph')
plt.legend()
plt.show()


# In[31]:


# Recover default matplotlib settings
mpl.rcParams.update(mpl.rcParamsDefault)
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(9,9))
area = [48 , 30 , 20 , 15]
labels = ['Low' , 'Medium' , 'High' , 'Critical']
colors = ['#8BC34A','#D4E157','#FFB300','#FF7043']
plt.pie (area , labels= labels , colors= colors , startangle=45)
plt.show()


# In[34]:


plt.figure(figsize=(9,9))
area = [48 , 30 , 20 , 15]
labels = ['Low' , 'Medium' , 'High' , 'Critical']
colors = ['#8BC34A','#D4E157','#FFB300','#FF7043']
plt.pie (area , labels= labels , colors= colors , startangle=45)
my_circle=plt.Circle( (0,0), 0.7, color='white') # Adding circle at the centre
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.show()


# In[35]:


# Changing background color
fig = plt.figure(figsize=(9,9))
fig.patch.set_facecolor('#DADADA') # Changing background color of donut chart
area = [48 , 30 , 20 , 15]
labels = ['Low' , 'Medium' , 'High' , 'Critical']
colors = ['#8BC34A','#D4E157','#FFB300','#FF7043']
plt.pie (area , labels= labels , colors= colors , startangle=45)
my_circle=plt.Circle( (0,0), 0.7, color='#DADADA') # Adding circle at the centre
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.show()


# In[40]:


fig = plt.figure(figsize=(20,6))
area = [48 , 30 , 20 , 15]
priority = ['Low' , 'Medium' , 'High' , 'Critical']
status = ['Resolved' , 'Cancelled' , 'Pending' , 'Assigned']
company = ['IBM' , 'Microsoft', 'BMC' , 'Apple']
colors = ['#8BC34A','#D4E157','#FFB300','#FF7043']
plt.subplot(1,3,1)
plt.pie (area , labels= priority , colors= colors , startangle=45)
my_circle=plt.Circle( (0,0), 0.7, color='white') # Adding circle at the centre
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.subplot(1,3,2)
plt.pie (area , labels= status , colors= colors , startangle=45)
my_circle=plt.Circle( (0,0), 0.7, color='white') # Adding circle at the centre
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.subplot(1,3,3)
plt.pie (area , labels= company , colors= colors , startangle=45)
my_circle=plt.Circle( (0,0), 0.7, color='white') # Adding circle at the centre
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.show()


# In[41]:


fig = plt.figure(figsize=(20,13))
area = [48 , 30 , 20 , 15]
priority = ['Low' , 'Medium' , 'High' , 'Critical']
status = ['Resolved' , 'Cancelled' , 'Pending' , 'Assigned']
company = ['IBM' , 'Microsoft', 'BMC' , 'Apple']
colors = ['#8BC34A','#D4E157','#FFB300','#FF7043']
plt.subplot(2,3,1)
plt.pie (area , labels= priority , colors= colors , startangle=45)
my_circle=plt.Circle( (0,0), 0.7, color='white') # Adding circle at the centre
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.subplot(2,3,2)
plt.pie (area , labels= status , colors= colors , startangle=45)
my_circle=plt.Circle( (0,0), 0.7, color='white') # Adding circle at the centre
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.subplot(2,3,3)
plt.pie (area , labels= company , colors= colors , startangle=45)
my_circle=plt.Circle( (0,0), 0.7, color='white') # Adding circle at the centre
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.subplot(2,3,4)
plt.pie (area , labels= priority , colors= colors , startangle=45)
my_circle=plt.Circle( (0,0), 0.7, color='white') # Adding circle at the centre
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.subplot(2,3,5)
plt.pie (area , labels= status , colors= colors , startangle=45)
my_circle=plt.Circle( (0,0), 0.7, color='white') # Adding circle at the centre
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.subplot(2,3,6)
plt.pie (area , labels= company , colors= colors , startangle=45)
my_circle=plt.Circle( (0,0), 0.7, color='white') # Adding circle at the centre
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.show()


# In[42]:


x = np.random.normal(size = 2000)
plt.hist(x, bins=40, color='yellowgreen')
plt.gca().set(title='Histogram', ylabel='Frequency')
plt.show()


# In[44]:


# Using Edge Color for readability
plt.figure(figsize=(10,8))
x = np.random.normal(size = 2000)
plt.hist(x, bins=40, color='yellowgreen' , edgecolor="#6A9662")
plt.gca().set(title='Histogram', ylabel='Frequency')
plt.show()


# In[45]:


# Using Histogram to plot a cumulative distribution function
plt.figure(figsize=(10,8))
x = np.random.rand(2000)
plt.hist(x, bins=30 ,color='#ffa41b' , edgecolor="#639a67",cumulative=True)
plt.gca().set(title='Histogram', ylabel='Frequency')
plt.show()


# In[46]:


x = np.arange(1,31)
y = np.random.normal(10,11,size=30)
y = np.square(y)
plt.figure(figsize=(16,6))
plt.fill_between( x, y, color="#baf1a1") # #Changing Fill color
plt.plot(x, y, color='#7fcd91') # Color on edges
plt.title("$ Area $ $ chart $" , fontsize = 16)
plt.xlabel("$X$" , fontsize = 16)
plt.ylabel("$Y$" , fontsize = 16)
plt.show()

