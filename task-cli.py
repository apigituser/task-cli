import sys
import os
import json
import datetime

timestamp = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")

def list_tasks():
    with open("tasks.json") as file:
        tasks = json.load(file)
        
        for id,value in tasks.items():
            status = value['status']
            if len(sys.argv) <= 2:
                print(f"{id}. {value['description']}")
            elif sys.argv[2] == status:
                print(f"{id}. {value['description']}")

def add_task():
    task_description = sys.argv[2]
    task = {1: {
                "description": task_description, 
                "status": "todo", 
                "createdAt": timestamp, 
                "updatedAt": timestamp
                }
            }
    
    if(os.stat("tasks.json").st_size == 0):
        with open("tasks.json", "w") as file:
            json.dump(task, file)
    else:
        with open("tasks.json", "r+") as file:
            json_data = json.load(file)
            id = len(json_data) + 1
            task = {id: task.get(1)}
            json_data.update(task)
            file.seek(0)
            json.dump(json_data, file)

def delete_task():
    id = str(sys.argv[2])

    with open("tasks.json","r+") as file:
        data = json.load(file)
        if data.pop(id, None) == None:
            print("Task not found")
            return 1
        file.seek(0)
        file.truncate()
        json.dump(data, file)

def update_task():
    id = sys.argv[2]
    description = sys.argv[3]
    with open("tasks.json", "r+") as file:
        data = json.load(file)
        value = data.get(id, None)
        if value == None:
            print("Task not found")
            return 1
        value['description'] = description
        value['updatedAt'] = timestamp
        file.seek(0)
        file.truncate()
        json.dump(data, file)

def mark_task():
    id = sys.argv[2]
    mark = sys.argv[1]

    with open("tasks.json", "r+") as file:
        data = json.load(file)
        value = data.get(id, None)
        if value == None:
            print("Task not found")
            return 1
        value['updatedAt'] = timestamp
        match mark:
            case "mark-done":
                value['status'] = "done"
            case "mark-in-progress":
                value['status'] = "in-progress"
        file.seek(0)
        file.truncate()
        json.dump(data,file)

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