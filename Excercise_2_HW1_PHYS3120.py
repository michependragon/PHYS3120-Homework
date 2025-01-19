#!/usr/bin/env python
# coding: utf-8

# # PHYS 3120: Homework 1, Michelle Ukiwe

# ## Excercise 2
# Exercise 2 (50 points): Return to the initial commit in the repository by checking out the main branch. Modify the Jupyter notebook to perform the following tasks, while briefly describing what you are doing in text blocks above the code.
# 
# 

# ### Part (a)
# Using numpy, create a 100x3 array with random numbers that represents 100 position vectors in Cartesian coordinates.

# In[11]:


#importing numpy
import numpy as np

#creating an array called povecs that has 100 rows and 3 columns representing 100 position vectors in cartesian coordinates
povecs = np.random.rand(100,3)


# In[12]:


#displaying the position vectors
povecs


# ### Part (b)  
# Using matplotlib, create a scatter plot of the (x,z) coordinates. Label your axes!

# In[17]:


#importing matplotlib
import matplotlib.pyplot as plt

#selecting the first column of povecs and naming it xcoordinates
#note: [:, x] selects columns, [x,:] selects rows
xcoord = povecs[:,0]
#print the x coordinates
xcoord


# In[18]:


#displaying the z axis of the cartesian coordinates
zcoord = povecs[:,2]
zcoord


# In[20]:


#creating a scatter plot of the x and z coordinates
plt.scatter(xcoord,zcoord)

#labeling the title of the plot 
plt.title('Scatter Plot of (x,z) Coordinates')

#naming axes
plt.xlabel('x-axis')

plt.ylabel('z-axis')


# ### Part (c)
# Create a function that converts Cartesian coordinates to cylindrical coordinates.

# In[53]:


#creating a function titles cartesian to cylindrical that inputs the position vectors cartesian coordinates and outputs cylindrical coordinates
def cartesian_to_cylindrical(povecs):
    "this function converts x,y,z cartesian coordinates to cylindrical coordinates"
    #gathering each axes values by seperating povecs into 3 seperate columns
    xcoord = povecs[:,0]
    ycoord = povecs[:,1]
    zcoord = povecs[:,2]

    #gathering the radial coordinate by taking the square root of the sum of an x coordinate squared added to corresponding y coordinate squared
    r = np.sqrt(xcoord**2 + ycoord**2)
    #finding theta by taking inverse tangent of y divided by x
    θ = np.arctan(ycoord,xcoord)
    #z coordinate remains the same
    z = zcoord
    #combining these columns together to create cylindrical coordinates
    cylincoord = np.column_stack((r,θ,z))
    #return cylindrical coordinates
    return cylincoord



# In[54]:


#creating an array entitles cylindrical using the cartesian to cylindrical coordinates function
cylindrical = cartesian_to_cylindrical(povecs)
cylindrical


# ### Part (d)
# Using numpy, compute the mean, minimum, and maximum values of the radial coordinate.

# In[55]:


#taking the first column of the cylindrical coordinates array, which represents the radial coordinate
radial = cylindrical[:,1]
#numpy mean function to display mean
np.mean(radial)



# In[56]:


#finding the minimum 
np.min(radial)


# In[57]:


#displaying the maximum
np.max(radial)


# #### End of Assignment
