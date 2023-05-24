#Desktop script to create a simple Todo List
import sys

print(sys.version_info) #Must be Python 3.10 for match function.

todos = []

while True:
    user = input("Type add, show, edit, complete or exit: ")
    user = user.strip() #Remove spacing
    match user:
        case 'add':
            todo=input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                item = item.title()
                textf=f"{index+1} -> {item}"
                print(textf)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo=input("Enter a new todo: ")
            todos[number]=new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            number = number - 1
            todos.pop(number)
        case 'exit':
            break
        case _:
            print("Unknown command")