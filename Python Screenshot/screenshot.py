


# this script is written by pengchao in shanghai

# this script is for module pyscreenshot

import pyscreenshot # type: ignore

#image = pyscreenshot.grab(bbox=(x1,x2,y1,y2))

#image = pyscreenshot.grab(bbox=(100, 100, 500, 500))

image = pyscreenshot.grab()

image.show()

image.save("D:/myscreen.png")


