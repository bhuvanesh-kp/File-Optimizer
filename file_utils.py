import os
import random

def list_files(directory):
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
