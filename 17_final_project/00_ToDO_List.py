from modules.myTodo import ToDo_List
from modules.myTask import Task
from modules.mypriority import Priority
import os
import platform




todo = ToDo_List()
todo.load_from_csv()
print(todo)

def clear_console():
    # Check the operating system and run the appropriate command
    if platform.system() == "Windows":
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/macOS

def print_main_menu(todo):
    clear_console()
    print("_________________________________________")
    print(f"Todo list have {todo.len()} tasks for you!")
    print("_________________________________________")
    print("1 - add new task")
    print("2 - remove task")
    print("3 - show tasks")
    print("4 - save as")
    print("_________________________________________")
    print("Press 'Q' To Close The App")
    print("_________________________________________")
    return

def print_new_task_menu():
    clear_console()
    print("_________________________________________")
    name = input("enter the name: ")
    prio = input("enter a char for priority\n(H = high, M = medium, L = low): ")
    if prio == "H": prio = Priority.High
    elif prio == "M": prio = Priority.Medium
    elif prio == "L": prio = Priority.Low
    else:  prio = Priority.Unknown
    desc = input("enter descri: ")
    print("_________________________________________")
    return name, prio, desc

def print_remove_task_menu(todo):
    todo_list = todo.todo_list
    for i in range(len(todo_list)):
        print(f"{i} - {todo_list[i]}")
    print("_________________________________________")
    index = input("Enter index of the task you want to delet: ")
    try:
        index = int(index)
    except:
        index = len(todo_list)
    if(index < len(todo_list)):
        todo.remove_task(index)
    else:
        print("_________________________________________")
        input(f"Index is greater than {len(todo_list) - 1 if(len(todo_list) - 1)>=0 else 0} \nPress enter for main menu:")
    todo.save_to_csv()
    return

def print_save_as_menu(todo):
    print("_________________________________________")
    name = input("please enter file name without .csv: ")
    print("_________________________________________")
    try:
        todo.save_to_csv(filename=name+".csv")
        input(f"File saved as {name}.csv, \npress enter to go to main menu:")
    except:
        input("name include bad char, \npress enter to go to main menu:")
    

while True:
    print_main_menu(todo)
    goto = input("enter page number: ")
    if goto == "1":
        name, prio, desc = print_new_task_menu()
        newtask = Task(name, prio, desc)
        todo.add_task(newtask)
        todo.save_to_csv()

    elif goto == "2":
        clear_console()
        print_remove_task_menu(todo)

        pass
    elif goto == "3":
        clear_console()
        print(todo)
        input("press enter for main menu: ")
    elif goto == "4":
        clear_console()
        print_save_as_menu(todo)
    elif goto =="Q" or goto == "q":
        break
    else:
        pass
    pass
