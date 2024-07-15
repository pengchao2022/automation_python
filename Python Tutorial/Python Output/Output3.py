
import time

count_seconds = 300

for i in reversed(range(count_seconds + 1 )):
    if i > 0:
        print(i, end='>>>')
        time.sleep(2)

    else:
        print('Start')
