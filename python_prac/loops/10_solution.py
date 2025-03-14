import time  # Import the time module to introduce delays

# Initial wait time in seconds
wait_time = 1  

# Maximum number of retries
max_tries = 5  

# Counter to track the number of attempts
attempts = 0  

# Loop until the number of attempts reaches max_tries
while attempts < max_tries:
    # Print the current attempt number and wait time
    print(f"Attempts: {attempts + 1} Wait time: {wait_time}")

    # Pause execution for the current wait time
    time.sleep(wait_time)  

    # Double the wait time for the next attempt (exponential backoff)
    wait_time *= 2  

    # Increment the attempt counter
    attempts += 1  
