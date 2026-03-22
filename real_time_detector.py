
import os, time
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from detector import predict_file

FOLDER_TO_MONITOR = "C:/Users/Nithya/Documents"  # safer than whole system

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"[ALERT] File Created: {event.src_path}")
            self.check_file(event.src_path)
    def on_modified(self, event):
        if not event.is_directory:
            print(f"[ALERT] File Modified: {event.src_path}")
            self.check_file(event.src_path)
    def on_deleted(self, event):
        if not event.is_directory:
            print(f"[ALERT] File Deleted: {event.src_path}")
    def check_file(self, file_path):
        try:
            prediction = predict_file(file_path)
            if prediction == 1:
                print(f"[WARNING] Suspicious activity detected: {file_path}")
        except:
            pass

def monitor_processes():
    for proc in psutil.process_iter(['pid','name','open_files']):
        try:
            files = proc.info['open_files']
            if files:
                for f in files:
                    pred = predict_file(f.path)
                    if pred == 1:
                        print(f"[ALERT] Process {proc.info['name']} accessing file: {f.path}")
                        # Optional: proc.kill()
        except:
            continue

if __name__ == "__main__":
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, FOLDER_TO_MONITOR, recursive=True)
    observer.start()
    print(f"[INFO] Monitoring all files in: {FOLDER_TO_MONITOR}")

    try:
        while True:
            monitor_processes()
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
