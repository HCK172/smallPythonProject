F1 = "todo/todo.txt"
F2 = "todo/done.txt"

def get_todos(filepath=F1): 
    """Read a text file and return the list of to-do items"""
    with open(filepath, 'r') as file_local: 
        todos_local = file_local.readlines()
    return todos_local 

def get_done(filepath=F2):
    with open(filepath,'r') as file_local:
        done_local = file_local.readlines()
    return done_local

def write_todos(todos_arg, filepath=F1):
     with open(filepath, 'w') as file: 
        file.writelines(todos_arg)

def write_done(done_arg,filepath=F2):
     with open(filepath, 'w') as file: 
        file.writelines(done_arg)


if __name__ == "__main__":
    print(get_done())