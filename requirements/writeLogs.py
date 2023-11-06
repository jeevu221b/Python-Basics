import datetime


def writeInfos(message):
    with open("infoLogs.txt", "a") as f:
        f.write(message)
        
def writeErrors(message):
    with open("errorLogs.txt", "a") as f:
        f.write(message)
        

def infoLogs(message):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M")
    messageToWrite = f"Time = {formatted_time}\nMessage = {message} \n\n"
    writeInfos(messageToWrite)
    
def errorsLogs(message):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M")
    messageToWrite = f"Time = {formatted_time}\nErrorMessage = {message} \n\n"
    writeErrors(messageToWrite)
    
    
    
