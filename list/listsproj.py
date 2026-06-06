tasks = []

while True:
    task = input("Enter task: ")

    if task == "quit":
        break

    tasks.append(task)

print("\nTasks:")

for task in tasks :
    print(task)