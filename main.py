import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "**Please drink water",
            message = "Time to drink water",
            timeout = 15
        )
        time.sleep(60*60)