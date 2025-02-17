import os
import shutil

def delete_directory(path):
    """
    Delete a directory and all its contents.

    Args:
        path (str): The relative or absolute path to the directory to be deleted.

    Raises:
        FileNotFoundError: If the directory does not exist.
        PermissionError: If the user lacks permissions to delete the directory.
        NotADirectoryError: If the path is not a directory.
        OSError: For other OS-related errors during deletion.
    """
    # Validate input
    if not isinstance(path, str):
        raise TypeError("Path must be a string")
    
    # Convert to absolute path to ensure consistent behavior
    abs_path = os.path.abspath(path)
    
    # Check if path exists
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"Directory not found: {path}")
    
    # Check if it's actually a directory
    if not os.path.isdir(abs_path):
        raise NotADirectoryError(f"Path is not a directory: {path}")
    
    try:
        # Use shutil.rmtree to recursively delete directory and contents
        shutil.rmtree(abs_path)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot delete directory {path}")
    except OSError as e:
        raise OSError(f"Error deleting directory {path}: {str(e)}")