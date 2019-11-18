tasks = open('todos.txt')
for chore in tasks:
    # print(chore)
    print(chore, end='')
tasks.close()
