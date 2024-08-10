#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess

def is_windows():
    return sys.platform.startswith('win')

def get_script_path():
    return os.path.dirname(os.path.realpath(__file__))

def find_dyspython_file():
    script_dir = get_script_path()
    for filename in os.listdir(script_dir):
        if filename.startswith('dyspython'):
            return os.path.join(script_dir, filename)
    raise FileNotFoundError("Could not find dyspython file in the current directory.")

def setup_unix():
    home = os.path.expanduser("~")
    bin_dir = os.path.join(home, "bin")
    dyspython_source = find_dyspython_file()
    dyspython_dest = os.path.join(bin_dir, "dyspython")

    os.makedirs(bin_dir, exist_ok=True)

    shutil.copy2(dyspython_source, dyspython_dest)
    os.chmod(dyspython_dest, 0o755)

    shell = os.environ.get("SHELL", "").split("/")[-1]
    rc_file = os.path.join(home, f".{shell}rc")

    path_export = f'\nexport PATH="$HOME/bin:$PATH"\n'
    with open(rc_file, 'r+') as f:
        content = f.read()
        if path_export not in content:
            f.seek(0, 2)  # Move to the end of the file
            f.write(path_export)

    print(f"DysPython installed/updated at {dyspython_dest}")
    print(f"Please restart your terminal or run 'source {rc_file}' to update your PATH.")

def setup_windows():
    scripts_dir = os.path.join(sys.prefix, "Scripts")
    dyspython_source = find_dyspython_file()
    dyspython_dest = os.path.join(scripts_dir, "dyspython.py")

    shutil.copy2(dyspython_source, dyspython_dest)

    bat_path = os.path.join(scripts_dir, "dyspython.bat")
    with open(bat_path, 'w') as f:
        f.write(f'@echo off\npython "{dyspython_dest}" %*')

    print(f"DysPython installed/updated at {dyspython_dest}")
    print("Please ensure your Python Scripts directory is in your PATH.")

def main():
    try:
        if is_windows():
            setup_windows()
        else:
            setup_unix()

        print("\nSetup complete! You can now use 'dyspython' to run your dysfunctional Python interpreter.")
        print("Usage: dyspython <script.py>")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure the dyspython file is in the same directory as this setup script.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()