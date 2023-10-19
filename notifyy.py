from notifypy import Notify
from datetime import datetime

user_time = "19:36:00"
current = datetime.now()
current_time = current.strftime("%H:%M:%S")
print(user_time)
print(current_time)
notification = Notify()
notification.title = "Price Watch Alert"
notification.message = "This is to verify that it works :)"
notification.application_name = "Price Watch"
notification.icon = "logo.png"
# while True:
#     if user_time == current_time:
#         notification.send()
#         break
#     current = datetime.now()
#     current_time = current.strftime("%H:%M:%S")

if user_time < current_time:
    print("Past")
elif user_time > current_time:
    print("Future")
else:
    print("Equal")
