import os
import shutil
from datetime import datetime


def create_backup(source_dir, destination_dir):
    # Check if source exists
    if not os.path.exists(source_dir):
        print(f"Source directory does not exist: {source_dir}")
        return

    # Create timestamped folder name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder_name = f"backup_{timestamp}"
    backup_path = os.path.join(destination_dir, backup_folder_name)

    try:
        # Create backup directory
        os.makedirs(backup_path)

        # Copy files
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            destination_item = os.path.join(backup_path, item)

            if os.path.isdir(source_item):
                shutil.copytree(source_item, destination_item)
            else:
                shutil.copy2(source_item, destination_item)

        print(f"Backup completed successfully at: {backup_path}")

    except Exception as e:
        print(f"Error during backup: {e}")


if __name__ == "__main__":
    print("=== Backup Automation Script ===")

    source = input("Enter the source directory path: ").strip()
    destination = input("Enter the destination directory path: ").strip()

    create_backup(source, destination)
