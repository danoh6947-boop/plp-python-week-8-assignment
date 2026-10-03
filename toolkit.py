"""
Power Toolkit - PLP Week 8 Project
A multi-tool Python utility program.
"""

import random

# --- TOOL 1: Number Guessing Game (Uses loops & conditionals) ---
def guess_number_tool():
    print("\n--- Number Guessing Game ---")
    secret = random.randint(1, 10)
    attempts = 3
    print("I'm thinking of a number between 1 and 10. You have 3 tries!")
    
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess == secret:
            print(f"🎉 Correct! The number was {secret}.")
            return
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")
        attempts -= 1
        print(f"Attempts left: {attempts}")
        
    print(f"Game over! The number was {secret}.\n")


# --- TOOL 2: To-Do / Shopping List (Uses dynamic list & loops) ---
def todo_list_tool():
    print("\n--- Quick Task List ---")
    tasks = []
    
    while True:
        item = input("Enter a task (or type 'done' to finish): ").strip()
        if item.lower() == 'done':
            break
        tasks.append(item)
        print(f"Added: '{item}'")
        
    print(f"\nYou have {len(tasks)} tasks:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")
    print()


# --- TOOL 3: Simple Calculator (Uses conditionals & f-strings) ---
def calculator_tool():
    print("\n--- Simple Calculator ---")
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ").strip()
    num2 = float(input("Enter second number: "))
    
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            return
        result = num1 / num2
    else:
        print("Invalid operator!")
        return

    print(f"Result: {num1} {op} {num2} = {result}\n")


# --- MAIN MENU LOOP ---
def main():
    print("=" * 35)
    print("   Welcome to the Power Toolkit!   ")
    print("=" * 35)
    
    while True:
        print("\nPlease choose a tool:")
        print("1. Number Guessing Game")
        print("2. Task / Shopping List")
        print("3. Simple Calculator")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            guess_number_tool()
        elif choice == "2":
            todo_list_tool()
        elif choice == "3":
            calculator_tool()
        elif choice == "4":
            print("\nThank you for using the Power Toolkit. Goodbye!")
            break
        else:
            print(f"⚠️ '{choice}' is not a valid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()