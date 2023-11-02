import datetime


def writeTo(message):
    with open("logs.txt", "a") as f:
        f.write(message)


def logs(message):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M")
    messageToWrite = f"Time = {formatted_time} and message = {message} \n\n"
    writeTo(messageToWrite)
