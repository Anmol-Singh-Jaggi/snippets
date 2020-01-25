import subprocess

from pathlib import Path

from shutil import copyfile
import sys


def git_backup(target_dir):
    """
    Copies all the untracked and modified files to a backup location.
    """
    target_dir = Path(target_dir)
    output = subprocess.run(["git", "status", "-vv"], capture_output=True, text=True)
    git_status_target_file = target_dir / "git_status_diff.txt"
    git_status_target_file.parent.mkdir(parents=True, exist_ok=True)
    with open(git_status_target_file, "w") as gits_target_file:
        gits_target_file.write(output.stdout)
    output = subprocess.run(
        ["git", "ls-files", "--modified", "--others", "--exclude-standard"],
        capture_output=True,
        text=True,
    )
    files_list = output.stdout.split()
    for file_src_path in files_list:
        file_target_path = target_dir / file_src_path
        print("src = " + file_src_path)
        print("target = " + str(file_target_path))
        file_target_path.parent.mkdir(parents=True, exist_ok=True)
        copyfile(file_src_path, file_target_path)


def main():
    # Usage:
    # 1. Put this script in your environ vars.
    # 2. cd into project directory.
    # 3. run `python git-backup.py /path/to/backup/dir`
    git_backup(sys.argv[1])


if __name__ == "__main__":
    main()
