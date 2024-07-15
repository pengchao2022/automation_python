

#import the libraries inputimeout, TimeoutOccurred

from inputimeout import inputimeout # type: ignore

try:

    time_over = inputimeout(prompt='Name your best friend:', timeout=1)

except Exception:

    time_over = 'Your time is over!'

    print(time_over)



