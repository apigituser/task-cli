import sys
import os
import json
import datetime

now = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")

def list_tasks():
    with open("tasks.json") as file:
        tasks = json.load(file)
        for id,value in tasks.items():
            status = tasks[id]['status']
            if len(sys.argv) <= 2:
                print(f"{id}. {value['description']}")
            elif sys.argv[2] == 'done':
                if status == 'done':
                    print(f"{id}. {tasks[id]['description']}")
            elif sys.argv[2] == 'todo':
                if status == 'todo':
                    print(f"{id}. {tasks[id]['description']}")
            elif sys.argv[2] == 'in-progress':
                if status == 'in-progress':
                    print(f"{id}. {tasks[id]['description']}")

def add_task():
    task_description = sys.argv[2]
    status = "todo"
    id = 1
    createdAt = str(now)
    updatedAt = str(now)
    task = {id: {
                "description": task_description, 
                "status": status, 
                "createdAt": createdAt, 
                "updatedAt": updatedAt
                }
            }
    check_file = os.stat("tasks.json").st_size
    if(check_file == 0):
        with open("tasks.json", "w") as file:
            json.dump(task, file)
    else:
        with open("tasks.json", "r+") as file:
            json_data:dict = json.load(file)
            id = len(json_data) + 1
            task = {id: {
                        "description": task_description, 
                        "status": status, 
                        "createdAt": createdAt, 
                        "updatedAt": updatedAt
                        }
                    }
            json_data.update(task)
            file.seek(0)
            json.dump(json_data, file)

def delete_task():
    id = str(sys.argv[2])

    with open("tasks.json") as file:
        data:dict = json.load(file)
        if data.pop(id, None) == None:
            print("Task not found")
    f = open("tasks.json", "w")
    json.dump(data,f)
    f.close()

def update_task():
    id = sys.argv[2]
    description = sys.argv[3]
    with open("tasks.json") as file:
        data:dict = json.load(file)
        value = data.get(id, None)
        if value == None:
            print("Task not found")
            return 1
        updatedAt = str(now)
        value['description'] = description
        value['updatedAt'] = updatedAt
    f = open("tasks.json","w")
    json.dump(data,f)
    f.close()

def mark_task():
    id = sys.argv[2]
    mark = sys.argv[1]

    with open("tasks.json") as file:
        data:dict = json.load(file)
        value = data.get(id, None)
        if value == None:
            print("Task not found")
            return 1
        updatedAt = str(now)
        value['updatedAt'] = updatedAt
        match mark:
            case "mark-done":
                value['status'] = "done"
            case "mark-in-progress":
                value['status'] = "in-progress"

    f = open("tasks.json","w")
    json.dump(data,f)
    f.close()

def main():
    if len(sys.argv) < 2:
        print("No command provided")
        return 1
    match sys.argv[1]:
        case "add":
            add_task()
        case "delete":
            delete_task()
        case "list":
            list_tasks()
        case "update":
            update_task()
        case "mark-done" | "mark-in-progress":
            mark_task()
        case _:
            print("Invalid Input")

if __name__ == "__main__":
    main()