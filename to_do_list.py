#Define a list to store tasks.
to_do_list = []

#Function to display to_do_list.
def display_list():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(to_do_list, start=1):
            print(f"{i}. {task}")

'''  function to add task to list
It take takes and add it to to_do_list'''
def add_task(task):
    to_do_list.append(task)
    print(f"Task '{task}' added to the list.")

'''  function to remove task from list
It take takes the task to remove and removes it from to_do_list'''
def remove_task(task_index):
    if 1 <= task_index <= len(to_do_list):
        removed_task = to_do_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the list.")
    else:
        print("Invalid task index.")
# while loop to take type of task from the user.
while True:
    print("\nOptions:")
    print("1. Show To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        display_list()
    elif choice == '2':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '3':
        display_list()
        task_index = int(input("Enter the task number to remove: "))
        remove_task(task_index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
