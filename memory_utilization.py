import psutil
import time
import logging

def memory_utilization_checker(interval=2, max_checks=None, log_to_file=False, log_file='memory_usage.log'):
    # Configure logging
    log_handlers = [logging.StreamHandler()]
    if log_to_file:
        log_handlers.append(logging.FileHandler(log_file))
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=log_handlers
    )

    check_count = 0
    try:
        while True:
            process = psutil.Process()
            mem_info = process.memory_info()
            virtual_memory = psutil.virtual_memory()

            logging.info("--- Memory Utilization ---")
            logging.info(f"Process Memory Usage: {mem_info.rss / (1024 ** 2):.2f} MB (RSS)")
            logging.info(f"Virtual Memory Total: {virtual_memory.total / (1024 ** 3):.2f} GB")
            logging.info(f"Virtual Memory Used: {virtual_memory.used / (1024 ** 3):.2f} GB")
            logging.info(f"Virtual Memory Available: {virtual_memory.available / (1024 ** 3):.2f} GB")
            logging.info(f"Memory Usage Percentage: {virtual_memory.percent}%")
            logging.info("--------------------------\n")

            check_count += 1
            if max_checks and check_count >= max_checks:
                logging.info("Reached maximum number of checks. Exiting.")
                break

            time.sleep(interval)
    except KeyboardInterrupt:
        logging.info("Memory utilization checker stopped by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage: log to console and file, check every 5 seconds, stop after 3 checks
    memory_utilization_checker(interval=5, max_checks=3, log_to_file=True)

# Unit test-trial example : #
import unittest
from unittest.mock import patch

class TestMemoryUtilizationChecker(unittest.TestCase):
    @patch('psutil.Process')
    @patch('psutil.virtual_memory')
    @patch('time.sleep', return_value=None)  # Skip actual sleep for faster test
    def test_checker_runs_and_stops(self, mock_sleep, mock_virtual_memory, mock_process):
        # Mock process.memory_info
        mock_process.return_value.memory_info.return_value = type('mem', (), {'rss': 1024 * 1024 * 100})()  # 100 MB
        # Mock virtual_memory
        mock_virtual_memory.return_value = type('vmem', (), {
            'total': 8 * 1024 ** 3,  # 8 GB
            'used': 4 * 1024 ** 3,   # 4 GB
            'available': 4 * 1024 ** 3,  # 4 GB
            'percent': 50.0
        })()

        # Run checker with max_checks=2 to test loop exit
        memory_utilization_checker(interval=0.1, max_checks=2, log_to_file=False)

if __name__ == '__main__':
    unittest.main()
