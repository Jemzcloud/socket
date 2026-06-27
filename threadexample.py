import threading

def scan(name):
    file = open(name, "r")
    print(file.read())
    file.close()
threads = []
for i in range(5):
    t = threading.Thread(target=scan, args=("test.txt",))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

