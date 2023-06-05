#Desktop script to create a simple Todo List
#This version, as the old one, uses if-else in order to type "add chore" 
#in one single instruction

import sys
import functions as fnct


while True:
    user = input("Type add, show, edit, complete or exit: ")
    user = user.strip() #Remove spacing
    
    if user.startswith('add'):
        todo = user[4:] #List slicing
        todos = fnct.get_todos()
        todos.append(todo+'\n')
        fnct.write_todos(todos)
    elif user.startswith('show'):
        todos=fnct.get_todos()
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
            todos = fnct.get_todos()
            todos[number-1]=new_todo + '\n'
            fnct.write_todos(todos)
        except ValueError:
            print("Your command is not valid, edit expects a number")
            continue
    elif user.startswith('complete'):
        try:
            text = user[9:].strip()
            number = int(text)
            todos = fnct.get_todos()
            todos.pop(number - 1)
            fnct.write_todos(todos)
        except IndexError:
            print("The number is out of range")
            continue            
    elif user.startswith('exit'):
        break
    else:
        print("Unknown command")