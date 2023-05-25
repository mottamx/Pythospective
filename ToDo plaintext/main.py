#Desktop script to create a simple Todo List
#Currently there are so many repeated lines, will need to fix

import sys

#print(sys.version_info) #Must be Python 3.10 for match function.

while True:
    user = input("Type add, show, edit, complete or exit: ")
    user = user.strip() #Remove spacing
    match user:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            with open(r'D:\MScCarlos\Documents\GitHub\Pythospective\ToDo plaintext\todos.txt', 'r') as file:
                todos = file.readlines()
                todos.append(todo)
            with open(r'D:\MScCarlos\Documents\GitHub\Pythospective\ToDo plaintext\todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open(r'D:\MScCarlos\Documents\GitHub\Pythospective\ToDo plaintext\todos.txt', 'r') as file:
                todos = file.readlines()
            #new_todos=[item.strip('\n') for item in todos] #List comprehension   
            for index, item in enumerate(todos):
                item = item.strip('\n').title()
                textf=f"{index+1} -> {item}"
                print(textf)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo=input("Enter a new todo: ")
            with open(r'D:\MScCarlos\Documents\GitHub\Pythospective\ToDo plaintext\todos.txt', 'r') as file:
                todos = file.readlines()
            todos[number]=new_todo + '\n'
            with open(r'D:\MScCarlos\Documents\GitHub\Pythospective\ToDo plaintext\todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            with open(r'D:\MScCarlos\Documents\GitHub\Pythospective\ToDo plaintext\todos.txt', 'r') as file:
                todos = file.readlines()
            todos.pop(number - 1)
            with open(r'D:\MScCarlos\Documents\GitHub\Pythospective\ToDo plaintext\todos.txt', 'w') as file:
                file.writelines(todos)
        case 'exit':
            break
        case _:
            print("Unknown command")