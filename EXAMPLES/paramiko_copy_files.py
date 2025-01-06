import os
import paramiko
from paramiko import Transport, SFTPClient

# In real life, don't hard-code password in script -- do one of these:
# with open('my_secret_file.txt') as secret_in:
#     password = secret_in.read().restrip()
# password = os.getenv("REMOTE_PASSWORD")

REMOTE_DIR = 'text_files'

with Transport(('localhost', 22)) as transport:  # create paramiko Transport instance
    transport.connect(username='python', password='l0lz')  # connect to remote host
    sftp = SFTPClient.from_transport(transport)  # create SFTP client using Transport instance
    for item in sftp.listdir_iter():  # get list of items on default (login) folder (listdir_iter() returns an iterator)
        print(item)
    print('-' * 60)

    remote_files = sftp.listdir(REMOTE_DIR)  # delete remote dir if it exists
    print(f"remote_files: {remote_files}")
    if remote_files:
        for remote_file in remote_files:
            remote_path = os.path.join(REMOTE_DIR, remote_file)
            print(f"remote_path: {remote_path}")

            sftp.remove(remote_path)
        sftp.rmdir(REMOTE_DIR)

    # create remote dir
    sftp.mkdir(REMOTE_DIR)

    # sftp.put(local-file)
    # sftp.put(local-file, remote-file)
    remote_path = os.path.join(REMOTE_DIR, 'betsy.txt')  # create path for remote file
    sftp.put('../DATA/alice.txt', remote_path)  # create a folder on the remote host
    sftp.put('../DATA/alice.txt', 'alice.txt')
    sftp.get(remote_path, 'eileen.txt')  # copy a file to the remote host
    print(sftp.listdir(), '\n')
    print(sftp.listdir(REMOTE_DIR))
