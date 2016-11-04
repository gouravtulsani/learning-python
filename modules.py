import os
file = os.popen("ls /home/grv/programs/python")
for line in file:
    print(line,end=' ')