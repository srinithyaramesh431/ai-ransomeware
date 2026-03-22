from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler
import time
import csv
import os

class MonitorHandler(FileSystemEventHandler):

    def on_created(self, event):
        print("CREATED:", event.src_path)
        self.write_csv("created", event.src_path)

    def on_modified(self, event):
        print("MODIFIED:", event.src_path)
        self.write_csv("modified", event.src_path)

    def write_csv(self, event_type, path):
        with open("data1.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([event_type, path, time.time()])
            f.flush()

# 👇 absolute path (important)
path = os.path.abspath("test_folder")

print("Monitoring path:", path)

# create csv if not exists
if not os.path.exists("data1.csv"):
    open("data1.csv", "w").close()

observer = PollingObserver()   # 👈 CHANGE HERE
event_handler = MonitorHandler()
observer.schedule(event_handler, path, recursive=True)
observer.start()

print("Monitoring started...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()