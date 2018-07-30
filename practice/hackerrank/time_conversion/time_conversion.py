#!/usr/bin/env python3

import os
import sys

#
# Complete the timeConversion function below.
#
def time_conversion(s):
    am_or_pm = s[-2:]
    hrs_mins_secs = s[0:-2].split(':')

    if am_or_pm == 'AM' and hrs_mins_secs[0] == '12':
        hrs_mins_secs[0] = '00'

    elif am_or_pm == 'PM' and hrs_mins_secs[0] == '12':
        hrs_mins_secs[0] = '12'

    elif am_or_pm == 'PM':
        hr = str((int(hrs_mins_secs[0]) + 12) % 24)
        if len(hr) == 1:
            hr = "0" + hr

        hrs_mins_secs[0] = hr

    return ":".join(hrs_mins_secs)
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = time_conversion(s)

    f.write(result + '\n')

    f.close()
