import threading

file = open("README.md", 'r')
line = True

def readLine():
    global line
    if line:
        threading.Timer(1.0, readLine).start()        
    line = file.readline()
    print(line)

threading.Timer(1.0, readLine).start()
file.close()