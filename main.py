import os
import time

def print_env_vars():
    # Iterate through the environment variables and print them
    for key, value in os.environ.items():
        print(f"{key}: {value}")

def main():
    print_env_vars()
    print("Starting the job 20 seconds...")
    time.sleep(20)
    print("I am done!")

if __name__ == "__main__":
    main()
