from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import sys


def post_reel():
    print("Starting Instagram Auto Poster...")
    subprocess.run([sys.executable, "-m", "app.main"])


scheduler = BlockingScheduler(timezone="Asia/Kolkata")

# Monday - Friday at 7:00 PM
scheduler.add_job(
    post_reel,
    trigger="cron",
    day_of_week="mon-fri",
    hour=19,
    minute=0,
)

# Saturday & Sunday at 10:30 AM
scheduler.add_job(
    post_reel,
    trigger="cron",
    day_of_week="sat,sun",
    hour=10,
    minute=30,
)

# Saturday & Sunday at 7:00 PM
scheduler.add_job(
    post_reel,
    trigger="cron",
    day_of_week="sat,sun",
    hour=19,
    minute=0,
)

print("Instagram Auto Poster Scheduler Started...")
scheduler.start()