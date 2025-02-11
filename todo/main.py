## how the data is stored -> store in a txt file
## function for showing the list of todos we have

import functions
import time 
#import functions import get_todos, get_done, write_done,write_todos
#import functions from other py file; has to be in the same folder
#import functions only, but have to add - function.(functions)
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    todos = functions.get_todos()
    done = functions.get_done()

    if user_action == 'add' or user_action == 'edit' or user_action=='complete':
            print(f'{user_action} what?')
    
    elif user_action.startswith('add'): 
        try: 
            todo = user_action[3:] 
            todo = todo.lstrip()
            todos.append(todo + '\n')
            print('Successfully added!')
            ### print(todos)

            functions.write_todos(todos)

        except ValueError:
            print('Your Command is not valid.')
            continue
    
    elif user_action.startswith('show'): 

        ## new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1} - {item} " 
                print(row)

    elif user_action.startswith('edit'): 
        
        try: 
            number = int(user_action[4:])
            #number = int(input('Number of the todo to edit:'))
            number = number - 1
            todos[number] = True
        
        except ValueError: 
             print('Please enter a number')
             continue
        except IndexError:
             print('There is no item for that number.') 
             continue

        todos[number] = input('Enter the new todo: ') + '\n'
        print('You have successfully edit the todo.')

        functions.write_todos(todos)
       
            

    elif user_action.startswith('done') or user_action.startswith('complete'): 
        
        try:
            num = int(user_action[8:])
            done.append(todos[num-1])
            write_done('todo/done.txt', done)

            todos.pop(num-1) 
            print('Yayy! you finished something today!')
            functions.write_todos('todo/todo.txt', todos)

            
        except IndexError:
             print('There is no item with that number.')
             continue

    elif user_action.startswith('exit'): 

        break

    else: 
         print("Command doesn't exist!")


