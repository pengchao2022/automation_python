# this program is to remove non-empty folders using python

# use the shutil module to remove non-empty folders

import shutil
import os
import time

location = "D:\\"

dir = "Inventory"

path = os.path.join(location,dir)

shutil.rmtree(path)

time.sleep(2)

print("Directory '%s' has been removed successfully" %dir)







