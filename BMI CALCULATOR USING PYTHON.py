#!/usr/bin/env python
# coding: utf-8

# In[1]:


h=float(input("enter your height: "))
w=float(input("enter your weight: "))
h = h/100
bmi = w/(h*h)
print("Your bmi is: ", bmi)
if(bmi>0):
    if(bmi<=16):
        print("Youre severely under weight")
    elif(bmi<=18.5):
        print("Youre under weight")
    elif(bmi<=25):
        print("Youre fit")
    elif(bmi<30):
        print("Youre overweight")
    elif(bmi<35):
        print("Youre obese")  
    else:
        print("fatally obese")
else:
    print("Invalid bmi")


# In[ ]:




