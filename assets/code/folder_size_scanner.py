import os
import sys
from pathlib import Path
import argparse
from datetime import datetime

def get_folder_size(folder_path):
    """Calculate the total size of a folder in bytes."""
    total_size = 0
    try:
        for path, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(path, file)
                try:
                    total_size += os.path.getsize(file_path)
                except (FileNotFoundError, PermissionError):
                    pass  # Skip files that can't be accessed
    except (PermissionError, OSError):
        pass  # Skip folders that can't be accessed
    return total_size

def format_size(size_bytes):
    """Convert size in bytes to a human-readable format."""
    # Define size units
    units = ('B', 'KB', 'MB', 'GB', 'TB')
    
    # Calculate appropriate unit
    i = 0
    while size_bytes >= 1024 and i < len(units) - 1:
        size_bytes /= 1024
        i += 1
    
    # Return formatted size
    return f"{size_bytes:.2f} {units[i]}"

def scan_directory(start_path, min_size_gb=5, output_file=None):
    """Scan directory and list folders larger than the specified size."""
    if not os.path.exists(start_path):
        print(f"Error: Path '{start_path}' does not exist")
        return
    
    print(f"Scanning {start_path} for folders larger than {min_size_gb} GB...")
    print("This may take some time depending on the size of the directory structure.")
    
    min_size_bytes = min_size_gb * 1024 * 1024 * 1024
    large_folders = []
    
    # Walk through directory structure
    for dirpath, dirnames, filenames in os.walk(start_path):
        try:
            dir_size = get_folder_size(dirpath)
            if dir_size >= min_size_bytes:
                large_folders.append((dirpath, dir_size))
                print(f"Found large folder: {dirpath} - {format_size(dir_size)}")
        except Exception as e:
            print(f"Error accessing {dirpath}: {e}")
    
    # Sort by size (largest first)
    large_folders.sort(key=lambda x: x[1], reverse=True)
    
    # Print results
    print("\n" + "="*80)
    print(f"FOLDERS LARGER THAN {min_size_gb} GB:")
    print("="*80)
    
    results = []
    for folder_path, size in large_folders:
        line = f"{format_size(size)}\t{folder_path}"
        results.append(line)
        print(line)
    
    # Write to output file if specified
    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"Scan performed on {timestamp}\n")
                f.write(f"Folders larger than {min_size_gb} GB:\n\n")
                for line in results:
                    f.write(line + "\n")
            print(f"\nResults saved to {output_file}")
        except Exception as e:
            print(f"Error writing to output file: {e}")
    
    print(f"\nFound {len(large_folders)} folders larger than {min_size_gb} GB")

def main():
    parser = argparse.ArgumentParser(description='Scan for large folders on your computer')
    parser.add_argument('--path', '-p', type=str, default='/', 
                        help='Starting path for the scan (default: root directory)')
    parser.add_argument('--size', '-s', type=float, default=5.0,
                        help='Minimum folder size in GB (default: 5 GB)')
    parser.add_argument('--output', '-o', type=str, 
                        help='Output file path to save results (optional)')
    
    args = parser.parse_args()
    
    # Adjust default path for Windows
    if sys.platform == 'win32' and args.path == '/':
        args.path = 'C:\\'
    
    scan_directory(args.path, args.size, args.output)

if __name__ == "__main__":
    main()
