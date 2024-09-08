import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print("Mudança detectada. Reiniciando...")
            os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
