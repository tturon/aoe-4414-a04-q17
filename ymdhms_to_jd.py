# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
# Converting year, month, day, hour, minute, second to fractional Julian date

# Parameters:
# year: year of interest, integer
# month: month of interest, integer
# day: day of interest, integer
# hour: hour of interest, integer
# minute: minute of interest, integer
# second: second of interest, float

# Output:
#  A description of the script output
#
# Written by Thomas Turon
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules

import sys
import math

# initialize Python modules
year = ''
month = ''
day = ''
hour = ''
minute = ''
second = ''

if len(sys.argv) == 7:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
else:
    print('Usage: python3 ymdhms_to_jd.py year month day hour minute second')
    exit()

#write script below this line

jd = day - 32075 + 1461*(year + 4800 - (14 - month)//12)//4 + 367*(month - 2 + (14 - month)//12*12)//12 - 3*((year + 4900 - (14 - month)//12)//100)//4
jdmidnight = jd - 0.5
dfrac = (second + 60*(minute + 60*hour))/86400
jd_frac = jdmidnight + dfrac

# print output results
print(jd_frac)