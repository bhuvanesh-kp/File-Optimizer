import os
import subprocess

def update_path_variable(group_name, new_files):
    path_dir = os.path.dirname(new_files[0])
    if os.name == 'nt':
        subprocess.run(f'setx PATH "%PATH%;{path_dir}"', shell=True)
    else:
        with open(os.path.expanduser("~/.bashrc"), "a") as f:
            f.write(f'\nexport PATH="$PATH:{path_dir}"\n')
