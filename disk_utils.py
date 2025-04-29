import shutil

def find_best_drive():
    drives = ['C:\\', 'D:\\', 'E:\\']  # or dynamic using psutil.disk_partitions()
    best = max(drives, key=lambda d: shutil.disk_usage(d).free)
    return best
