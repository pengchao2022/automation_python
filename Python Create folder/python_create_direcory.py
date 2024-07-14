#Python create folder 
# importing os module  
import os
import time
   
# Directory 
directory = "Python_DevOps1"
   
# Parent Directory path 
parent_dir = "D:\\"
   
# Path 
path = os.path.join(parent_dir, directory) 
   
# Create the directory 
# 'Python_Devops' in 
# 'D:\' root directory in D driver 
os.mkdir(path) 
time.sleep(2)

print("Directory '%s' created" %directory)
