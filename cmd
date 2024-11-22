import subprocess
import psutil
import time

# Global variable to keep track of the cmd process
cmd_process = None

def open_cmd():
    global cmd_process
    try:
        # Open Command Prompt and store the process
        cmd_process = subprocess.Popen('cmd.exe')
        print("Command Prompt opened.")
    except Exception as e:
        print(f"An error occurred: {e}")

def close_cmd():
    global cmd_process
    if cmd_process is not None:
        try:
            # Terminate the Command Prompt process
            cmd_process.terminate()  # Gracefully terminate
            cmd_process.wait()       # Wait for the process to terminate
            print("Command Prompt closed.")
            cmd_process = None  # Reset the cmd_process variable
        except Exception as e:
            print(f"An error occurred while closing cmd: {e}")
    else:
        print("No Command Prompt is currently open.")

if __name__ == "__main__":
    print("Welcome to Jarvis! Type 'open cmd' to open the Command Prompt, 'close cmd' to close it.")
    
    while True:
        command = input("You: ").strip().lower()
        
        if command == "open cmd":
            open_cmd()
        elif command == "close cmd":
            close_cmd()
        elif command == "exit":
            print("Exiting Jarvis. Goodbye!")
            break
        else:
            print("Unknown command. Please try again.")
