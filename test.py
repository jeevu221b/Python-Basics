from datetime import datetime

# Get the current date and time
current_time = datetime.now()

# Print the current time in the default format (including date and time)
print("Current Time:", current_time)

# If you want to display only the time without the date
current_time_str = current_time.strftime("%H:%M:%S")
print("Current Time (hh:mm:ss):", current_time_str)
