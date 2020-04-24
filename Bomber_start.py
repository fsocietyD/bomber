from Bomber_own_class import Bomber

print("Welcome to Bomber")
count = int(input("Enter count of processes: "))
iteration = int(input("Enter count of iteration (one process): "))
for _ in range(count):
    thread = Bomber(iteration)
    thread.start()
print("ALL PROCESSES WERE STARTED")