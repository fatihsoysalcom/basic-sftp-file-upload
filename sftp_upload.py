import pysftp
import os

# --- Configuration ---
# Replace with your SFTP server details
SFTP_HOST = "your_sftp_host"
SFTP_PORT = 22
SFTP_USERNAME = "your_username"
SFTP_PASSWORD = "your_password" # Consider using SSH keys for better security

# Local file to upload
LOCAL_FILE_PATH = "./local_file_to_upload.txt"

# Remote path on the SFTP server where the file will be uploaded
REMOTE_FILE_PATH = "/remote/directory/local_file_to_upload.txt"

# --- Create a dummy local file for demonstration ---
def create_dummy_file(filepath):
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            f.write("This is a test file for SFTP upload.\n")
        print(f"Created dummy file: {filepath}")

# --- Main SFTP Upload Function ---
def upload_file_sftp(host, port, username, password, local_path, remote_path):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None # WARNING: This disables host key checking, use with caution in production

    try:
        print(f"Connecting to SFTP server at {host}:{port}...")
        with pysftp.Connection(host, port=port, username=username, password=password, cnopts=cnopts) as sftp:
            print("Connection successful.")

            # Ensure the remote directory exists (optional, but good practice)
            remote_dir = os.path.dirname(remote_path)
            if not sftp.exists(remote_dir):
                print(f"Creating remote directory: {remote_dir}")
                sftp.makedirs(remote_dir)

            # Upload the file
            print(f"Uploading {local_path} to {remote_path}...")
            sftp.put(local_path, remote_path)
            print("File uploaded successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# --- Execution ---
if __name__ == "__main__":
    create_dummy_file(LOCAL_FILE_PATH)
    # Ensure you have replaced the placeholder credentials and paths above
    if SFTP_HOST == "your_sftp_host":
        print("\n!!! Please update SFTP_HOST, SFTP_USERNAME, SFTP_PASSWORD, and file paths in the script before running. !!!\n")
    else:
        upload_file_sftp(SFTP_HOST, SFTP_PORT, SFTP_USERNAME, SFTP_PASSWORD, LOCAL_FILE_PATH, REMOTE_FILE_PATH)
