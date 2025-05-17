from modules.myTask import Task
from modules.mypriority import Priority
import csv

class ToDo_List:
    todo_list_id = 0
    def __init__(self):
        '''یک لیست شامل تمام تسک های شئ ساخته شده'''
        self.todo_list = []
        '''شناسه تودو لیست که با هر بار ساخته شدن یک شی از این کلاس یکی به شماره آن اضافه میشود'''
        self.id = ToDo_List.todo_list_id
        ToDo_List.todo_list_id +=1

    def add_task(self, task):
        '''کار جدید را به تسک تودو لیست اضافه میکند.'''
        self.todo_list.append(task)
        return len(self.todo_list)

    def remove_task(self, task):
        self.todo_list.pop(task)
        return task
    def show_tasks():
        pass

    def __str__(self):
        text = ""
        for i in range(len(self.todo_list)):
            text+= f"{i} - {self.todo_list[i]}"
        return text
    def len(self):
        return len(self.todo_list)
    

    def save_to_csv(self, filename = "task.csv"):
         with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for task in self.todo_list:
                name, prio, desc = task.to_list()
                writer.writerow([name, prio.name, desc])
        
    def load_from_csv(self, filename = "task.csv"):
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                self.todo_list = [Task(row[0], Priority[row[1]], row[2]) for row in reader]
        except FileNotFoundError:
            print(f"{filename} not found. Starting with an empty list.")