from notifypy import Notify

def notifier(task):
    notification = Notify()
    notification.title = "Task Scheduler"
    notification.message = ""
    notification.application_name = task
    notification.icon = "logo.png"
    notification.send()
