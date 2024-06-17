# todo_list.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the list.")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def update_task(self, task_number, new_task):
        try:
            task_number = int(task_number)
            if task_number < 1 or task_number > len(self.tasks):
                print("Invalid task number.")
            else:
                self.tasks[task_number - 1] = new_task
                print(f"Task {task_number} updated to '{new_task}'.")
        except ValueError:
            print("Invalid task number.")

    def delete_task(self, task_number):
        try:
            task_number = int(task_number)
            if task_number < 1 or task_number > len(self.tasks):
                print("Invalid task number.")
            else:
                del self.tasks[task_number - 1]
                print(f"Task {task_number} deleted.")
        except ValueError:
            print("Invalid task number.")

def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            task_number = input("Enter the task number to update: ")
            new_task = input("Enter the new task: ")
            todo.update_task(task_number, new_task)
        elif choice == "4":
            task_number = input("Enter the task number to delete: ")
            todo.delete_task(task_number)
        elif choice == "5":
            print("Have a great day, Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()






#password_generator.py

import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_punctuation=True):
    all_characters = string.ascii_lowercase
    if use_uppercase:
        all_characters += string.ascii_uppercase
    if use_digits:
        all_characters += string.digits
    if use_punctuation:
        all_characters += string.punctuation
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    use_uppercase = input("Use uppercase letters? (y/n) ").lower() == 'y'
    use_digits = input("Use digits? (y/n) ").lower() == 'y'
    use_punctuation = input("Use punctuation? (y/n) ").lower() == 'y'
    password = generate_password(length, use_uppercase, use_digits, use_punctuation)
    if password:
        print("Generated Password : ", password)

if __name__ == "__main__":
    main()







#rock_papper_scissors_game.py

import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer's choice: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "yes":
            break

def play_game(user_score, computer_score):
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer's choice: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    print(f"Score - You: {user_score}, Computer: {computer_score}")
    return user_score, computer_score

def main():
    user_score = 0
    computer_score = 0
    while True:
        user_score, computer_score = play_game(user_score, computer_score)
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
