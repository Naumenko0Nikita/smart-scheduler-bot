import os, sys ,time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess


class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script_path):
        self.script_path = script_path
        self.process = None
        self.restart_script()

    def restart_script(self):
        if self.process:
            self.process.kill()
        print("Restarting...")
        self.process = subprocess.Popen([sys.executable, self.script_path])

    def on_modified(self, event):
        if event.src_path.endswith("config.py"):
            self.restart_script()

if __name__ == "__main__":
    path_to_watch = "modules/config.py"
    script_to_run = "manage.py"

    event_handler = ReloadHandler(script_to_run)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(path_to_watch), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
