import psutil ## pip install psutil ##
import time ## pip install time ##

def memory_utilization_checker(interval=2, max_checks=None):
    check_count = 0
    try:
        while True:
            process = psutil.Process()
            mem_info = process.memory_info()
            virtual_memory = psutil.virtual_memory()

            print(f"--- Memory Utilization ---")
            print(f"Process Memory Usage: {mem_info.rss / (1024 ** 2):.2f} MB (RSS)")
            print(f"Virtual Memory Total: {virtual_memory.total / (1024 ** 3):.2f} GB")
            print(f"Virtual Memory Used: {virtual_memory.used / (1024 ** 3):.2f} GB")
            print(f"Virtual Memory Available: {virtual_memory.available / (1024 ** 3):.2f} GB")
            print(f"Memory Usage Percentage: {virtual_memory.percent}%")
            print("--------------------------\n")

            check_count += 1
            if max_checks and check_count >= max_checks:
                print("Reached maximum number of checks. Exiting.")
                break

            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMemory utilization checker stopped by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    print("Starting memory utilization checker. Press Ctrl+C to stop.")
    memory_utilization_checker(interval=5, max_checks=None)  # Set max_checks to an int to limit runs
