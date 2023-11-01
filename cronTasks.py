import sqlite3
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import notifier
import time

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

scheduler = BackgroundScheduler()


# @TO_DO: Take userId as a parameter
def getDueTasks():
    allTasks = []
    t = datetime.now()
    curr_time = t.strftime("%H:%M:%S")
    cursor.execute("SELECT * FROM tasks")
    #    where duedate > ?", (curr_time,))
    tasks = cursor.fetchall()
    for ids in tasks:
        __task = {
            "user_id": ids[0],
            "task_id": ids[1],
            "taskname": ids[2],
            "duedate": ids[3],
        }
        allTasks.append(__task)
    print(allTasks)
    return allTasks


def cronos():
    scheduler.add_job(getDueTasks, "interval", seconds=3)
    scheduler.start()


while True:
    cronos()
    time.sleep(1)


# ids = getDueTasks()

# for id in ids:
#     duedate = id["duedate"]
#     taskname = id["taskname"]
#     time_obj = datetime.strptime(duedate, "%H:%M:%S")
#     hour = time_obj.hour
#     minute = time_obj.minute
#     second = time_obj.second
#     print(taskname)
#     cronJob(hour, minute, second, taskname)
#     print("Hey!")

# if __name__ == "__main__":
#     scheduler.start()
#     try:
#         while True:
#             pass
#     except (KeyboardInterrupt, SystemExit):
#         scheduler.shutdown()


# def cronJob(hr, min, sec, taskname):
#     scheduler.add_job(
#         notifier.notifier, "cron", hour=hr, minute=min, second=sec, args=[taskname]
#     )
