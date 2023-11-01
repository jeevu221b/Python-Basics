import sqlite3
# Import the correct scheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import notifyy
# conn = sqlite3.connect("app.db")
# cursor = conn.cursor()
scheduler = BackgroundScheduler()


def getDueTasks():

    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    allTasks = []
    t = datetime.now()
    curr_time = t.strftime("%H:%M:%S")
    cursor.execute("SELECT * FROM tasks WHERE duedate > ?", (curr_time,))
    tasks = cursor.fetchall()
    for ids in tasks:
        __task = {
            "task_id": ids[0],
            "user_id": ids[1],
            "taskname": ids[2],
            "duedate": ids[3],
        }
        allTasks.append(__task)
    print(allTasks)
    return allTasks

# getDueTasks()


# def cronJob(hr, min, sec, taskname):
#     scheduler.add_job(
#         notifyy.notifier, "cron", hour=hr, minute=min, second=sec, args=[taskname]
#     )


def cronos():
    print("Inside cronos")
    # Create a BlockingScheduler instance
    cronScheduler = BlockingScheduler()

    # Schedule the getDueTasks function to run every 3 seconds (adjust the interval as needed)
    cronScheduler.add_job(getDueTasks, 'interval', seconds=3)

    # Start the scheduler
    print("Yoppie")
    cronScheduler.start()
    print("Yippie")

    ids = getDueTasks()
    print(f"Length = {len(ids)}")

    for id in ids:
        duedate = id["duedate"]
        taskname = id["taskname"]
        time_obj = datetime.strptime(duedate, "%H:%M:%S")
        hour = time_obj.hour
        minute = time_obj.minute
        second = time_obj.second
        # cronJob(hour, minute, second, taskname)
        print("Hey!")


if __name__ == '__main__':
    cronos()


# ids = getDueTasks()
# print(f"Length = {len(ids)}")

# for id in ids:
#     duedate = id["duedate"]
#     taskname = id["taskname"]
#     time_obj = datetime.strptime(duedate, "%H:%M:%S")
#     hour = time_obj.hour
#     minute = time_obj.minute
#     second = time_obj.second
#     cronJob(hour, minute, second, taskname)
#     print("Hey!")

# if __name__ == "__main__":
#     scheduler.start()
#     try:
#         while True:
#             pass
#     except (KeyboardInterrupt, SystemExit):
#         scheduler.shutdown()
