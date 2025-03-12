import click  # Click is a package used to create command-line interfaces (CLI)
import json  # JSON is used to store and retrieve data in JSON format
import os  # OS module helps interact with the operating system, such as checking if a file exists

# Constant variable for the JSON file that stores tasks
TODO_FILE = "todo.json" 

# Function to load tasks from the JSON file
def load_task():
    if not os.path.exists(TODO_FILE):  # Check if the JSON file exists
        return []  # If the file doesn't exist, return an empty list (no tasks available)
    with open(TODO_FILE, "r") as file:  # Open the file in read mode
        return json.load(file)  # Load and return the JSON data as a Python object (list of tasks)

# Function to save tasks into the JSON file
def save_task(task):
    with open(TODO_FILE, "w") as file:  # Open the file in write mode
        json.dump(task, file, indent=4)  # Write tasks into the file with proper indentation for readability

# Grouping all functions under a single command-line interface (CLI) using Click
@click.group()
def cli():
    """Simple Todo List Manager"""
    pass  # This function acts as a container for CLI commands

# Command to add a new task to the list
@click.command()
@click.argument("task")  # Accepts a task as an argument from the command line
def add(task):
    """Add new task to the list"""
    tasks = load_task()  # Load existing tasks
    tasks.append({"task": task, "done": False})  # Append a new task with 'done' set to False
    save_task(tasks)  # Save updated tasks back to the JSON file
    click.echo(f"Task added successfully: {task}")  # Print a success message

# Command to list all tasks
@click.command()
def list():
    """List all tasks"""
    tasks = load_task()  # Load existing tasks
    if not tasks:  # Check if the task list is empty
        click.echo("No tasks found")  # Display message if no tasks exist
        return
    for index, task in enumerate(tasks, 1):  # Loop through tasks with index starting from 1
        status = "✅" if task["done"] else "❌"  # Mark task as completed or not
        click.echo(f"{index}. {task['task']} [{status}]")  # Display task with status

# Command to mark a task as completed
@click.command()
@click.argument("task_number", type=int)  # Accepts a task number as an integer argument
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_task()  # Load existing tasks
    if 0 < task_number <= len(tasks):  # Validate if the task number is within the correct range
        tasks[task_number - 1]["done"] = True  # Mark the task as completed
        save_task(tasks)  # Save updated tasks back to the JSON file
        click.echo(f"Task {task_number} marked as completed!")  # Print success message
    else:
        click.echo("Invalid task number.")  # Print error message if task number is invalid

# Command to remove a task from the list
@click.command()
@click.argument("task_number", type=int)  # Accepts a task number as an integer argument
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_task()  # Load existing tasks
    if 0 < task_number <= len(tasks):  # Validate if the task number is within range
        removed_task = tasks.pop(task_number - 1)  # Remove the task from the list
        save_task(tasks)  # Save updated tasks back to the JSON file
        click.echo(f"Removed task: {removed_task['task']}")  # Print confirmation message
    else:
        click.echo("Invalid task number")  # Print error message if task number is invalid

# Adding all commands to the CLI group
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

# Entry point for the program
if __name__ == "__main__":
    cli()  # Run the command-line interface
