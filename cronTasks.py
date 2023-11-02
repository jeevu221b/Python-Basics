import sqlite3
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from notifyy import notifier
from log import logs
from log import writeTo

# Create a BackgroundScheduler instance for the getDueTasks function

# with open("logs.txt", "a") as f:
cronScheduler = BackgroundScheduler()
cronScheduler.start()

# Create a BackgroundScheduler instance for the cron jobs
scheduler = BackgroundScheduler()
scheduler.start()


def getDueTasks():
    # with open("logs.txt", "a") as f:
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
    message = f"All tasks = {allTasks}"
    logs(message)
    if len(allTasks) <= 0:
        message = "No due tasks"
        logs(message)
    # Check with cron if any of these tasks are already scheduled.
    all_jobs = scheduler.get_jobs()
    job_id = [job.id for job in all_jobs]
    # print(job_id)
    for id in allTasks:
        task_id = id["task_id"]
        duedate = id["duedate"]
        # message = f"Taskid = {task_id}, Jobid = {job_id}"
        # print(message, file=f)
        try:
            if str(task_id) not in job_id:
                message = f"Scheduling cron job for task_id -->{task_id}"
                logs(message)
                duedate = id["duedate"]
                taskname = id["taskname"]
                time_obj = datetime.strptime(duedate, "%H:%M:%S")
                hour = time_obj.hour
                minute = time_obj.minute
                second = time_obj.second
                cronJob(task_id, hour, minute, second, taskname)
                message = f"Cron job scheduled for task = {taskname} at hr = {hour},at min = {minute},with task_id = {task_id}"
                logs(message)
            else:
                # message = (
                #     f"Cron job already scheduled for taskid ={task_id} at {duedate}"
                # )
                # logs(message)
                pass
        except Exception as a:
            print(f"ERROR = {a}")


def cronJob(taskid, hr, min, sec, taskname):
    scheduler.add_job(
        notifier,
        "cron",
        id=str(taskid),
        hour=hr,
        minute=min,
        second=sec,
        args=[taskname],
    )


def cronos():
    cronScheduler.add_job(getDueTasks, "interval", seconds=15)


if __name__ == "__main__":
    cronos()
    try:
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        cronScheduler.shutdown()
