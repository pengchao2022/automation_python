# Python program to explain shutil.copyfile() method 
# importing shutil module 
import shutil 

# Source path 
source = "C:/Users/penma/Downloads/VMware-workstation-17.5.2-23775571.exe"

# Destination path 
destination = "C:/Users/penma/PythonTest/python2024/vm1.exe"

dest = shutil.copyfile(source, destination) 

print("Destination path:", dest) 
