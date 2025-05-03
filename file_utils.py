import os
import random
from pathlib import Path

def list_files(directory):
    list_of_folders = []
    lsit_of_files = []

    path = Path(directory)
    for item in path.iterdir():
        if item.is_dir():
            list_of_folders.append(item)
        elif item.is_file():
            lsit_of_files.append(item)

    print(f"[INFO] Found {len(list_of_folders)} folders and {len(lsit_of_files)} files in {directory}.\n")
    return list_of_folders, lsit_of_files

    try:
        return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except Exception as e:
        print(f"[ERROR] {e}")
        return []

def sample_file_contents(files, sample_size=3):
    sampled_files = random.sample(files, min(sample_size, len(files)))
    samples = []
    for path in sampled_files:
        try:
            with open(path, "r", errors="ignore") as f:
                content = f.read(512)
                samples.append((path, content))
        except Exception as e:
            print(f"[WARNING] Cannot read file: {path}. Reason: {e}")
    return samples
