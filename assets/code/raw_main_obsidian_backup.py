# config.py - Configuration file for the backup script

# --- Paths ---
# !! IMPORTANT: Replace these placeholder paths with your actual paths !!
# Use forward slashes '/' even on Windows

# Path to your Obsidian vault directory
VAULT_PATH = "C:/Users/YourUser/Documents/Obsidian Vault"

# Path to the folder where local backups should be stored
LOCAL_BACKUP_DIR = "D:/Backups/Obsidian"

# Full path to the Obsidian executable
# Windows example: "C:/Users/YourUser/AppData/Local/Obsidian/Obsidian.exe"
# macOS example: "/Applications/Obsidian.app/Contents/MacOS/Obsidian"
# Linux example: "/usr/bin/obsidian" or similar (use 'which obsidian' in terminal)
OBSIDIAN_EXECUTABLE_PATH = "C:/Users/YourUser/AppData/Local/Obsidian/Obsidian.exe"

# --- Google Drive ---
# Name of the folder in Google Drive where backups should be uploaded
# The script will create this folder if it doesn't exist.
GDRIVE_BACKUP_FOLDER_NAME = "Obsidian Backups"

# Path to the 'credentials.json' file downloaded from Google Cloud Console
# See setup instructions below.
GDRIVE_CREDENTIALS_FILE = "C:/path/to/your/credentials.json"

# Path to store the token file after successful authorization
GDRIVE_TOKEN_FILE = "token.json"

# --- Settings ---
# Backup filename format (uses datetime formatting)
# Example: vault_backup_20250426_133000.zip
BACKUP_FILENAME_FORMAT = "vault_backup_%Y%m%d_%H%M%S.zip"

# --- END OF CONFIGURATION ---

# ==============================================================================
# backup_and_launch.py - Main script (Save this as a separate file)
# ==============================================================================

import os
import sys
import shutil
import zipfile
import datetime
import subprocess
import config  # Imports the config.py file

# --- Google Drive Imports ---
# You need to install these: pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# --- Constants ---
SCOPES = ['https://www.googleapis.com/auth/drive.file'] # Scope for uploading files

# --- Helper Functions ---

def _log(message):
    """Simple logging function."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def _check_paths():
    """Validate essential paths from config."""
    if not os.path.isdir(config.VAULT_PATH):
        _log(f"ERROR: Obsidian Vault path not found: {config.VAULT_PATH}")
        sys.exit(1)
    if not os.path.exists(config.OBSIDIAN_EXECUTABLE_PATH):
        _log(f"ERROR: Obsidian executable not found: {config.OBSIDIAN_EXECUTABLE_PATH}")
        sys.exit(1)
    if not os.path.exists(config.GDRIVE_CREDENTIALS_FILE):
         _log(f"ERROR: Google Drive credentials file not found: {config.GDRIVE_CREDENTIALS_FILE}")
         _log("Please follow setup instructions to get 'credentials.json'.")
         sys.exit(1)
    # Create local backup dir if it doesn't exist
    os.makedirs(config.LOCAL_BACKUP_DIR, exist_ok=True)
    _log("Configuration paths checked.")

def zip_vault(output_zip_path):
    """Zips the entire Obsidian vault directory."""
    _log(f"Starting vault zip process for: {config.VAULT_PATH}")
    try:
        with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(config.VAULT_PATH):
                # Don't include the .obsidian/workspace.json or workspace-mobile.json
                # as these change frequently and contain session state.
                # You might want to customize excluded files/folders further.
                dirs[:] = [d for d in dirs if d not in ['.git', '.trash']] # Example exclusions
                files[:] = [f for f in files if f not in ['workspace.json', 'workspace-mobile.json']]

                for file in files:
                    file_path = os.path.join(root, file)
                    # Calculate arcname relative to vault path
                    arcname = os.path.relpath(file_path, config.VAULT_PATH)
                    zipf.write(file_path, arcname)
        _log(f"Vault successfully zipped to: {output_zip_path}")
        return True
    except Exception as e:
        _log(f"ERROR: Failed to zip vault: {e}")
        return False

def backup_local(zip_file_path):
    """Copies the zip file to the local backup directory."""
    if not os.path.exists(zip_file_path):
        _log(f"ERROR: Zip file not found for local backup: {zip_file_path}")
        return False
    try:
        destination_path = os.path.join(config.LOCAL_BACKUP_DIR, os.path.basename(zip_file_path))
        shutil.copy2(zip_file_path, destination_path) # copy2 preserves metadata
        _log(f"Local backup successful: {destination_path}")
        return True
    except Exception as e:
        _log(f"ERROR: Failed to create local backup: {e}")
        return False

def authenticate_gdrive():
    """Handles Google Drive authentication."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists(config.GDRIVE_TOKEN_FILE):
        try:
            creds = Credentials.from_authorized_user_file(config.GDRIVE_TOKEN_FILE, SCOPES)
        except Exception as e:
            _log(f"Warning: Could not load token file '{config.GDRIVE_TOKEN_FILE}': {e}. Re-authenticating.")
            creds = None # Force re-authentication

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                _log("Refreshing Google Drive credentials...")
                creds.refresh(Request())
            except Exception as e:
                _log(f"ERROR: Failed to refresh token: {e}")
                _log("Attempting full re-authentication.")
                creds = None # Force re-authentication
        else:
             _log("Google Drive credentials not found or invalid. Starting authentication flow...")
             try:
                flow = InstalledAppFlow.from_client_secrets_file(config.GDRIVE_CREDENTIALS_FILE, SCOPES)
                # Run local server temporarily for OAuth flow
                creds = flow.run_local_server(port=0)
                _log("Authentication successful.")
             except FileNotFoundError:
                 _log(f"ERROR: Credentials file not found at {config.GDRIVE_CREDENTIALS_FILE}")
                 return None
             except Exception as e:
                 _log(f"ERROR: Authentication flow failed: {e}")
                 return None
        # Save the credentials for the next run
        try:
            with open(config.GDRIVE_TOKEN_FILE, 'w') as token:
                token.write(creds.to_json())
            _log(f"Credentials saved to {config.GDRIVE_TOKEN_FILE}")
        except Exception as e:
            _log(f"ERROR: Could not save token file: {e}")
            # Continue anyway, but user might need to re-auth next time

    if creds and creds.valid:
        _log("Google Drive authentication successful.")
        return creds
    else:
        _log("ERROR: Could not obtain valid Google Drive credentials.")
        return None

def get_or_create_gdrive_folder(service, folder_name):
    """Finds a folder by name in Google Drive root, creates it if not found."""
    try:
        # Search for the folder
        query = f"mimeType='application/vnd.google-apps.folder' and name='{folder_name}' and 'root' in parents and trashed=false"
        response = service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
        folders = response.get('files', [])

        if folders:
            folder_id = folders[0].get('id')
            _log(f"Found Google Drive folder '{folder_name}' with ID: {folder_id}")
            return folder_id
        else:
            # Create the folder
            _log(f"Google Drive folder '{folder_name}' not found. Creating...")
            file_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            folder = service.files().create(body=file_metadata, fields='id').execute()
            folder_id = folder.get('id')
            _log(f"Created Google Drive folder '{folder_name}' with ID: {folder_id}")
            return folder_id
    except HttpError as error:
        _log(f"ERROR: An error occurred interacting with Google Drive folders: {error}")
        return None
    except Exception as e:
        _log(f"ERROR: Unexpected error getting/creating Google Drive folder: {e}")
        return None


def backup_gdrive(service, zip_file_path, folder_id):
    """Uploads the zip file to the specified Google Drive folder."""
    if not service:
        _log("ERROR: Google Drive service not available for upload.")
        return False
    if not os.path.exists(zip_file_path):
        _log(f"ERROR: Zip file not found for Google Drive backup: {zip_file_path}")
        return False
    if not folder_id:
        _log("ERROR: No valid Google Drive folder ID provided for upload.")
        return False

    try:
        _log(f"Starting Google Drive upload of: {os.path.basename(zip_file_path)}")
        file_metadata = {
            'name': os.path.basename(zip_file_path),
            'parents': [folder_id] # Specify the parent folder
        }
        media = MediaFileUpload(zip_file_path, mimetype='application/zip', resumable=True)
        request = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        )

        # Execute the upload with progress (optional but good for large files)
        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                _log(f"Google Drive Upload Progress: {int(status.progress() * 100)}%")

        _log(f"Google Drive backup successful. File ID: {response.get('id')}")
        return True

    except HttpError as error:
        _log(f"ERROR: An Google Drive API error occurred during upload: {error}")
        # Consider specific error handling (e.g., quota exceeded)
        return False
    except Exception as e:
        _log(f"ERROR: Failed to upload to Google Drive: {e}")
        return False

def launch_obsidian():
    """Launches the Obsidian application."""
    _log(f"Launching Obsidian: {config.OBSIDIAN_EXECUTABLE_PATH}")
    try:
        # Use Popen for non-blocking launch
        subprocess.Popen([config.OBSIDIAN_EXECUTABLE_PATH])
        _log("Obsidian launched successfully.")
    except FileNotFoundError:
        _log(f"ERROR: Obsidian executable not found at the specified path: {config.OBSIDIAN_EXECUTABLE_PATH}")
    except Exception as e:
        _log(f"ERROR: Failed to launch Obsidian: {e}")

# --- Main Execution ---
if __name__ == "__main__":
    _log("--- Starting Obsidian Backup & Launch Script ---")

    # 1. Check Configuration Paths
    _check_paths()

    # 2. Prepare Backup File Name and Path
    timestamp_str = datetime.datetime.now().strftime(config.BACKUP_FILENAME_FORMAT)
    temp_zip_filename = f"temp_{timestamp_str}" # Temporary name before copying/uploading
    # Store temporary zip in the script's directory or a dedicated temp folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    temp_zip_path = os.path.join(script_dir, temp_zip_filename)

    # 3. Zip the Vault
    if not zip_vault(temp_zip_path):
        _log("Halting script due to zip failure.")
        # Optionally launch Obsidian anyway? For now, we stop.
        # launch_obsidian()
        sys.exit(1) # Exit if zipping failed

    # 4. Perform Local Backup
    if not backup_local(temp_zip_path):
        _log("Local backup failed, but continuing with Google Drive backup and launch.")
        # Decide if this failure should prevent launch

    # 5. Authenticate and Backup to Google Drive
    gdrive_creds = authenticate_gdrive()
    if gdrive_creds:
        try:
            gdrive_service = build('drive', 'v3', credentials=gdrive_creds)
            _log("Google Drive service built successfully.")

            # Get target folder ID
            target_folder_id = get_or_create_gdrive_folder(gdrive_service, config.GDRIVE_BACKUP_FOLDER_NAME)

            if target_folder_id:
                 # Perform the upload
                if not backup_gdrive(gdrive_service, temp_zip_path, target_folder_id):
                    _log("Google Drive backup failed.")
                    # Decide if this failure should prevent launch
            else:
                 _log("Could not get or create Google Drive folder. Skipping Drive backup.")

        except Exception as e:
            _log(f"ERROR: An error occurred during Google Drive operations: {e}")
    else:
        _log("Skipping Google Drive backup due to authentication failure.")

    # 6. Clean up temporary zip file
    try:
        if os.path.exists(temp_zip_path):
            os.remove(temp_zip_path)
            _log(f"Cleaned up temporary zip file: {temp_zip_path}")
    except Exception as e:
        _log(f"Warning: Could not remove temporary zip file {temp_zip_path}: {e}")

    # 7. Launch Obsidian
    launch_obsidian()

    _log("--- Script finished ---")

