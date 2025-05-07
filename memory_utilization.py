import psutil ## pip install psutil ##
import time  ## pip install time ##
## (OR) ALTERNATIVE FOR TIME IS from datetime import time ##

def memory_utilization_checker(interval=2):    ## exceptional def memory_utilization_checker(): as the code for it ##
    while True:
        # Get the memory usage of the current process
        process = psutil.Process()
        mem_info = process.memory_info()
        
        # Get the virtual memory usage of the system
        virtual_memory = psutil.virtual_memory()
        
        print(f"--- Memory Utilization ---")
        print(f"Process Memory Usage: {mem_info.rss / (1024 ** 2):.2f} MB")  # Resident Set Size
        print(f"Virtual Memory Total: {virtual_memory.total / (1024 ** 2):.2f} MB")
        print(f"Virtual Memory Used: {virtual_memory.used / (1024 ** 2):.2f} MB")
        print(f"Virtual Memory Available: {virtual_memory.available / (1024 ** 2):.2f} MB")
        print(f"Memory Usage Percentage: {virtual_memory.percent}%")
        print("--------------------------")
        
        time.sleep(interval)  # Wait for the specified interval before checking again
        # or you can write it as time.sleep(2) #
if __name__ == "__main__":
    print("Starting memory utilization checker. Press Ctrl+C to stop.")
    try:
        memory_utilization_checker(interval=5)  # Check every 5 seconds
    except KeyboardInterrupt:
        print("\nMemory utilization checker stopped.")

