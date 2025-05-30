# Match-Case in Python
# This file shows how to use match-case statements (Python 3.10+)

# Example 1: Basic Match-Case
print("Example 1 - Basic Match-Case:")
status = "success"

match status:
    case "success":
        print("Operation completed successfully!")
    case "error":
        print("An error occurred!")
    case _:
        print("Unknown status")

# Example 2: Match-Case with Multiple Patterns
print("\nExample 2 - Match-Case with Multiple Patterns:")
command = "quit"

match command:
    case "start" | "begin":
        print("Starting the program...")
    case "stop" | "quit" | "exit":
        print("Stopping the program...")
    case _:
        print("Unknown command") 