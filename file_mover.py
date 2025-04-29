import shutil
import os

def move_files(file_list, destination_root, group_name):
    target_dir = os.path.join(destination_root, "Organized", group_name)
    os.makedirs(target_dir, exist_ok=True)
    
    moved_files = []
    for f in file_list:
        try:
            shutil.move(f, target_dir)
            moved_files.append(os.path.join(target_dir, os.path.basename(f)))
        except Exception as e:
            print(f"⚠️ Failed to move {f}: {e}")
    
    return moved_files
