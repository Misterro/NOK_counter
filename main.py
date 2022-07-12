import datetime
import re

f = open('events.txt')

# dict with summary
times = dict()

for line in f:
    # filter without NOK
    if line.find('NOK') >= 0:

        # regexp for found date and time
        raw = ' '.join(re.findall('\d*-\d*-\d*\s*\d*:\d*', line)[0].split())

        # convert to datatime
        date = datetime.datetime.strptime(raw, '%Y-%m-%d %H:%M')

        # count events
        if times.get(date) is None:
            times[date] = 1
        else:
            times[date] = times.get(date) + 1

# events output
for key, value in times.items():
    print("{} was {} events".format(key.isoformat(), value))
