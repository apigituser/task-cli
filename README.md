## Task-CLI TODO App
Task-CLI is a simplistic command line todo program. It records the tasks given by the user and also provides options to update them.

### Functionality
1. Add tasks
2. List all tasks
3. List tasks that are done
4. List tasks that are not done
5. List tasks that are in progress
6. Update task description
7. Update task status
8. Delete specific tasks

### Prerequisites
Python should be installed

You should know how to use the command line

### Installation Process
1. Clone this repository:

   ```
   git clone https://github.com/apigituser/task-cli
   ```
2. Go to the task-cli directory

   ```
   cd task-cli
   ```
3. Run the program using python

   ```
   python task-cli
   ```

### How To: Perform Operations
1. Add Task

   ```
   python task-cli.py add "Task Name"
   ```

2. List Tasks

   ```
   python task-cli.py list                // Lists all the tasks
   python task-cli.py list done           // Lists tasks that are done
   python task-cli.py list todo           // Lists tasks that are not done
   python task-cli.py list in-progress    // Lists tasks that are in-progress
   ```

3. Update Task
   > id is the task number
   ```
   python task-cli.py update <id> "New Task"  // Updating task description
   python task-cli.py mark-done <id>          // Marking task as done
   python task-cli.py mark-in-progress <id>   // Marking task as in-progress

6. Delete a Task

   ```
   python task-cli.py delete <id>
   ```

### Roadmap.sh Project URL
Project link is available [here](https://roadmap.sh/projects/task-tracker)
