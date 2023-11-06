from apscheduler.schedulers.background import BackgroundScheduler

# Create a BackgroundScheduler instance
scheduler = BackgroundScheduler()


# Define a function for a sample cron job
def cron_job1():
    print("Cron job 1 executed")


def cron_job2():
    print("Cron job 2 executed")


# Add cron jobs to the scheduler
scheduler.add_job(cron_job1, "cron", id="1", second="*/5")
scheduler.add_job(cron_job2, "cron", id="2", second="*/10")

# Start the scheduler
scheduler.start()

# List all running cron jobs
all_jobs = scheduler.get_jobs()
if all_jobs:
    print("List of Scheduled Jobs:")
    for job in all_jobs:
        print(job.id)
# Stop the scheduler (when you're done)
scheduler.shutdown()
