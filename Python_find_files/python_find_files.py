
# importing shutil module  
import shutil 
import time 
   
# file search  
file = 'JAVA'
   
# Using shutil.which() method 
locate = shutil.which(file) 
time.sleep(2)
   
# Print result 
print(locate)
