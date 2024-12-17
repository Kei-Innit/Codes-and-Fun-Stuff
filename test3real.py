import time
from datetime import datetime, timedelta

def calculate_next_hour():
    now = datetime.now()
    next_hour = now + timedelta(hours=1)
    next_hour = next_hour.replace(minute=0, second=0, microsecond=0)
    return next_hour

def main():
    next_hour = calculate_next_hour()
    print("Check your reward") 
    while True: # Code stops here while waiting for the time
        current_time = datetime.now()
        if current_time >= next_hour:
            next_hour = calculate_next_hour()
            reward_time = next_hour.strftime("%I:%M %p")
            print(f"Your reward will be available after the next hour, which is {reward_time}.")
            # Here, you can implement code to grant the reward
        time.sleep(10)  # Check every minute

if __name__ == "__main__":
    main()