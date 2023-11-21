import paramiko

def change_letter():
    # SSH Connection Details
    hostname = 'worker node-4'
    port = 22
    username = 'ayan'
    password = 'pass123'  # You may use key-based authentication for better security

    # Remote file path
    remote_file_path = '/root/test/new.txt'

    # Connect to the remote machine
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password)

    try:
        # Read the content of the remote file
        stdin, stdout, stderr = ssh.exec_command(f'cat {remote_file_path}')
        file_content = stdout.read().decode('utf-8')

        # Modify the content (replace 'i' with 'I')
        modified_content = file_content.replace('i', 'I')

        # Write the modified content back to the remote file
        with ssh.open_sftp() as sftp:
            with sftp.file(remote_file_path, 'w') as remote_file:
                remote_file.write(modified_content)

        # Download the modified file to the local machine
        local_file_path = 'new_modified.txt'
        with ssh.open_sftp() as sftp:
            sftp.get(remote_file_path, local_file_path)

        print("File modification and transfer successful.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the SSH connection
        ssh.close()

if __name__ == "__main__":
    change_letter()
