import sqlite3
from apscheduler.schedulers.background import BackgroundScheduler
from notifyy import Notify
from datetime import datetime

conn = sqlite3.connect("app.db")
cursor = conn.cursor()


def notifier(taskname):
    notification = Notify()
    notification.title = "Task Scheduler"
    notification.message = taskname
    notification.application_name = "jeevu"
    notification.icon = "logo.png"
    notification.send()


def getTaskid():
    task_ids = []
    t = datetime.now()
    curr_time = t.strftime("%H:%M:%S")
    cursor.execute("SELECT * FROM tasks where duedate > ?", (curr_time,))
    tasks = cursor.fetchall()
    for ids in tasks:
        task_ids.append(ids[0])
    return task_ids


scheduler = BackgroundScheduler()


def cronJob(hr, min, sec, taskname):
    scheduler.add_job(notifier, "cron", hour=hr, minute=min,
                      second=sec, args=[taskname])


ids = getTaskid()
for id in ids:
    print(id)
    cursor.execute("SELECT * FROM tasks where task_id = ?", (str(id),))
    trigger_task = cursor.fetchone()
    duedate = trigger_task[3]
    time_obj = datetime.strptime(duedate, "%H:%M:%S")
    hour = time_obj.hour
    minute = time_obj.minute
    second = time_obj.second
    taskname = trigger_task[2]
    print(taskname)
    cronJob(hour, minute, second, taskname)
    print("Hey!")

if __name__ == "__main__":
    scheduler.start()
    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
