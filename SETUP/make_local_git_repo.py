import sys
import os
from zipfile import ZipFile
import tarfile

ARCHIVE_BASE_NAME = "myproject"

def main():
    home_dir = os.path.expanduser('~')

    if sys.platform == 'win32':
        zip_file_path = f"{ARCHIVE_BASE_NAME}.zip"
        zip_archive = ZipFile(zip_file_path)
        zip_archive.extractall(home_dir)
    else:
        tar_file_path = f"{ARCHIVE_BASE_NAME}.tar.gz"
        with tarfile.open(tar_file_path) as tar_archive:
            tar_archive.extractall(home_dir)

if __name__ == "__main__":
    main()
