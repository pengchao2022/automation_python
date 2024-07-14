# Python program to explain shutil.copytree() method 
# importing os module 
import os 

# importing shutil module 
import shutil 
import time

# path 
path = 'C:/Users/penma/Downloads'

print("Before copying file:") 
print(os.listdir(path)) 

# Source path 
src = 'C:/Users/penma/Downloads/'

# Destination path 
dest = 'C:/Users/penma/myfiles/2024'

# Copy the content of 
# source to destination 
destination = shutil.copytree(src, dest) 

print("After copying file:") 
print(os.listdir(path)) 

# Print path of newly 
# created file 
print("Destination path:", destination) 
