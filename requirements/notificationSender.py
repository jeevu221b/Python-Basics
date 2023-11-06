from notifypy import Notify

def notifier(taskname):
    notification = Notify()
    notification.title = "Task Scheduler"
    notification.message = ""
    notification.application_name = taskname
    # notification.icon = "logo.png"
    notification.send()

