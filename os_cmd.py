'''
import os
for file in os.listdir("Downloads"):
    if file.endswith(".pdf"):
        os.rename(f"Downloads/{file}",f"Downloads/PDF_REPORT_{file}")
    elif file.endswith(".xlsx") or file.endswith(".ods"):
        os.rename(f"Downloads/{file}",f"Downloads/EXCEL_SPREADSHEET_REPORT_{file}")
    elif file.endswith(".exe"):
        os.rename(f"Downloads/{file}",f"Downloads/EXECUTABLE_FILE_{file}")
    elif file.endswith(".txt") or file.endswith(".docx"):
        os.rename(f"Downloads/{file}",f"Downloads/TEXT_DOCUMENT_{file}")
    elif file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
        os.rename(f"Downloads/{file}",f"Downloads/IMAGE_FILE_{file}")
    elif file.endswith(".mp4") or file.endswith(".mov"):
        os.rename(f"Downloads/{file}",f"Downloads/VIDEO_FILE_{file}")
    elif file.endswith(".zip") or file.endswith(".rar"):
        os.rename(f"Downloads/{file}",f"Downloads/COMPRESSED_ARCHIVE_{file}")  
    else:
        os.rename(f"Downloads/{file}",f"Downloads/OTHER_FILES_{file}")'''

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.rename_file(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.rename_file(event.src_path)

    def rename_file(self, file_path):
        try:
            file_name = os.path.basename(file_path)
            dir_path = os.path.dirname(file_path)
            
            # Skip temporary files
            if file_name.endswith('.tmp'):
                return
            
            # Skip if already renamed (check for prefixes)
            prefixes = ["PDF_REPORT_", "EXCEL_SPREADSHEET_REPORT_", "EXECUTABLE_FILE_", "TEXT_DOCUMENT_", "IMAGE_FILE_", "VIDEO_FILE_", "COMPRESSED_ARCHIVE_", "OTHER_FILES_"]
            if any(file_name.startswith(prefix) for prefix in prefixes):
                return
            
            if file_name.endswith(".pdf"):
                new_name = f"PDF_REPORT_{file_name}"
            elif file_name.endswith((".xlsx", ".ods")):
                new_name = f"EXCEL_SPREADSHEET_REPORT_{file_name}"
            elif file_name.endswith(".exe"):
                new_name = f"EXECUTABLE_FILE_{file_name}"
            elif file_name.endswith((".txt", ".docx")):
                new_name = f"TEXT_DOCUMENT_{file_name}"
            elif file_name.endswith((".png", ".jpg", ".jpeg")):
                new_name = f"IMAGE_FILE_{file_name}"
            elif file_name.endswith((".mp4", ".mov")):
                new_name = f"VIDEO_FILE_{file_name}"
            elif file_name.endswith((".zip", ".rar")):
                new_name = f"COMPRESSED_ARCHIVE_{file_name}"
            else:
                new_name = f"OTHER_FILES_{file_name}"
            
            new_path = os.path.join(dir_path, new_name)
            os.rename(file_path, new_path)
            print(f"Renamed {file_name} to {new_name}")
        except Exception as e:
            print(f"Error renaming file {file_path}: {e}")

if __name__ == "__main__":
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, downloads_dir, recursive=False)
    observer.start()
    print("Monitoring Downloads folder for new files...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()