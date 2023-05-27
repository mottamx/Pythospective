#Desktop script to create a simple Todo List
#This version, as the old one, uses if-else in order to type "add chore" 
#in one single instruction

import sys

#print(sys.version_info) #Must be Python 3.10 for match function.

while True:
    user = input("Type add, show, edit, complete or exit: ")
    user = user.strip() #Remove spacing
    
    if user.startswith('add'):
        todo = user[4:] #List slicing
        with open(r'D:\MScCarlos\Documents\GitHub\Pythospective\ToDo plaintext\todos.txt', 'r') as file:
            todos = file.readlines()
            todos.append(todo+'\n')
        with open(r'D:\MScCarlos\Documents\GitHub\Pythospective\ToDo plaintext\todos.txt', 'w') as file:
            file.writelines(todos)
    elif user.startswith('show'):
        with open(r'D:\MScCarlos\Documents\GitHub\Pythospective\ToDo plaintext\todos.txt', 'r') as file:
            todos = file.readlines()
        #new_todos=[item.strip('\n') for item in todos] #List comprehension   
        for index, item in enumerate(todos):
            item = item.strip('\n').title()
            textf=f"{index+1} -> {item}"
            print(textf)
    elif user.startswith('edit'):
        try:
            text = user[5:].strip()
            number = int(text)
            new_todo=input("Enter a new todo: ")
            with open(r'D:\MScCarlos\Documents\GitHub\Pythospective\ToDo plaintext\todos.txt', 'r') as file:
                todos = file.readlines()
            todos[number-1]=new_todo + '\n'
            with open(r'D:\MScCarlos\Documents\GitHub\Pythospective\ToDo plaintext\todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid, edit expects a number")
            continue
    elif user.startswith('complete'):
        try:
            text = user[9:].strip()
            number = int(text)
            with open(r'D:\MScCarlos\Documents\GitHub\Pythospective\ToDo plaintext\todos.txt', 'r') as file:
                todos = file.readlines()
            todos.pop(number - 1)
            with open(r'D:\MScCarlos\Documents\GitHub\Pythospective\ToDo plaintext\todos.txt', 'w') as file:
                file.writelines(todos)
        except IndexError:
            print("The number is out of range")
            continue            
    elif user.startswith('exit'):
        break
    else:
        print("Unknown command")