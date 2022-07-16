import os

import datetime
entries = os.listdir()
files = []


for entry in entries:
    stats = {}
    if entry.endswith('.jpg'):
        # files.append(entry)
        m_time = os.path.getmtime(entry)
        dt_m = datetime.datetime.fromtimestamp(m_time)
        # print(entry)
        # print('Modified on:', dt_m)
        stats["name"] = entry
        stats["time"] = str(dt_m)
        print(stats)
        files.append(stats)
files = sorted(files, key=lambda d: d['time'])             
print(files)

for i in range(len(files)):
    os.rename(files[i]['name'], str(i)+'.jpg')


# iterate over all files and then position 1 will be named 1 
    # print(entry)
    # print(os.path.getmtime(entry))
    # files[entry] = os.path.getmtime(entry)




