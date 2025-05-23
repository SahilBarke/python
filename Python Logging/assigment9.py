import logging
import time
import os
from logging.handlers import RotatingFileHandler

# Constants
NUM_MESSAGES = 100
LOG_MESSAGE = "This is a test log message number {}"

# Log file names
LOG_FILE = "benchmark_log.log"
ROTATING_LOG_FILE = "rotating_benchmark_log.log"

# Clean up old logs
for file in [LOG_FILE, ROTATING_LOG_FILE]:
    if os.path.exists(file):
        os.remove(file)

# Benchmark function
def benchmark_logging(handler, use_formatter=False):
    logger = logging.getLogger("BenchmarkLogger")
    logger.setLevel(logging.DEBUG)

    # Clear existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    handler.setLevel(logging.DEBUG)

    if use_formatter:
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

    logger.addHandler(handler)

    start = time.perf_counter()
    for i in range(NUM_MESSAGES):
        logger.debug(LOG_MESSAGE.format(i))
    end = time.perf_counter()

    return end - start

# Main benchmarking routine
def run_all_tests():
    print("Benchmarking logging handlers (time in seconds for {} messages):\n".format(NUM_MESSAGES))

    # Use lambdas to recreate fresh handler instances each time
    handler_constructors = {
        "Console Handler": lambda: logging.StreamHandler(),
        "File Handler": lambda: logging.FileHandler(LOG_FILE),
        "Rotating File Handler": lambda: RotatingFileHandler(ROTATING_LOG_FILE, maxBytes=1000000, backupCount=3)
    }

    for name, constructor in handler_constructors.items():
        # Run WITHOUT formatting
        handler_no_format = constructor()
        duration_no_format = benchmark_logging(handler_no_format, use_formatter=False)

        # Run WITH formatting
        handler_with_format = constructor()
        duration_with_format = benchmark_logging(handler_with_format, use_formatter=True)

        # Print benchmark results
        print(f"{name:<35} | Without Formatting: {duration_no_format:.4f} sec | With Formatting: {duration_with_format:.4f} sec")

if __name__ == "__main__":
    run_all_tests()
