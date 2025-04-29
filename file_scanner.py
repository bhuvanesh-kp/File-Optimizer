import os
import random

def list_files(directory):
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            all_files.append(os.path.join(root, file))
    return random.sample(all_files, min(3, len(all_files)))
