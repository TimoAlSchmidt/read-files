import time

with open("README.md", 'r') as file:
    line = True
    while line:
        line = file.readline()
        print(line)
        time.sleep(1)
