FILEPATH = r'ToDo plaintext\todos.txt'



def get_todos():
    """
    Function to copy the todo list from file to a list variable
    Returns: list containing the todo list
    """
    with open(FILEPATH, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_write):
    """
    Function to write the todo listo to a file
    """
    with open(FILEPATH, 'w') as file:
        file.writelines(todos_write)