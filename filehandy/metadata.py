import os
import platform
import stat
import time

# Package reliant
try:
    import magic
except ImportError:
    magic = None

def fetch_metadata(filepath: str) -> dict[str, str | int]:
    """
    Fetches metadata for the given file. Uses os.stat for Unix-like systems and
    pywin32 for Windows to get detailed metadata.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")

    file_stat = os.stat(filepath)

    metadata = {
        'size': file_stat.st_size,
        'last_accessed': time.ctime(file_stat.st_atime),
        'last_modified': time.ctime(file_stat.st_mtime),
        'creation_time': time.ctime(file_stat.st_ctime),  # On Unix, this is the time of last metadata change
        'mode': file_stat.st_mode,
        'inode': file_stat.st_ino,
        'device': file_stat.st_dev,
        'n_links': file_stat.st_nlink,
        'uid': file_stat.st_uid,
        'gid': file_stat.st_gid,
    }

    if magic:
        metadata["mime_type"] = magic.Magic(mime=True).from_file(filepath)
    else:
        metadata["mime_type"] = "Unknown"

    if platform.system() == 'Windows':
        # Additional Windows-specific metadata
        try:
            import win32file
            import win32con
            file_info = win32file.GetFileAttributesEx(filepath, win32con.GetFileExInfoStandard)
            metadata['creation_time'] = time.ctime(file_info[4])
            metadata['last_accessed'] = time.ctime(file_info[5])
            metadata['last_modified'] = time.ctime(file_info[6])
        except ImportError:
            print("pywin32 is not installed. Some Windows-specific metadata will not be available.")

    return metadata
