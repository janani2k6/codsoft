class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added successfully.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')

    def update_task(self, index, new_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = new_task
            print(f'Task {index} updated successfully.')
        else:
            print('Invalid task index.')

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            print(f'Task {index} ("{deleted_task}") deleted successfully.')
        else:
            print('Invalid task index.')

def main():
    todo_list = TodoList()
    while True:
        print('\n1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Exit')
        choice = input('Enter your choice (1-5): ')
        
        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input('Enter the task index to update: '))
            new_task = input('Enter the new task: ')
            todo_list.update_task(index, new_task)
        elif choice == '4':
            index = int(input('Enter the task index to delete: '))
            todo_list.delete_task(index)
        elif choice == '5':
            break
        else:
            print('Invalid choice, please enter a number between 1 and 5.')

if __name__ == "__main__":
    main()
