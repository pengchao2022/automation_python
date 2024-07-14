# Python program to explain os.removedirs() method 
	
# importing os module 
import os 
import time

# Leaf Directory name 
directory = "Inventory"

# Parent Directory 
parent = "D:\\"

# Path 
path = os.path.join(parent, directory) 

# Remove the Directory 
# "baz" 
os.removedirs(path) 

time.sleep(2)

print("Directory '%s' has been removed successfully" %directory) 

# All parent directory 
# of 'baz' will be also 
# removed if they are empty 

