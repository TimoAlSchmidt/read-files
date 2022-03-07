import threading

def readLine():
    with open("README.md", 'r') as file:
        line = file.readline()
        if line:
            line = file.readline()
            threading.Timer(1.0, readLine).start()
        print(line)

threading.Timer(1.0, readLine).start()