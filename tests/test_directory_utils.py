import os
import pytest
import tempfile
import shutil
from src.directory_utils import delete_directory

def test_delete_directory():
    # Create a temporary directory with some files and subdirectories
    with tempfile.TemporaryDirectory() as base_dir:
        # Create some nested directories and files
        os.makedirs(os.path.join(base_dir, 'subdir1', 'subsubdir'))
        os.makedirs(os.path.join(base_dir, 'subdir2'))
        
        # Create some files
        with open(os.path.join(base_dir, 'file1.txt'), 'w') as f:
            f.write('test')
        with open(os.path.join(base_dir, 'subdir1', 'file2.txt'), 'w') as f:
            f.write('test')
        
        # Use relative path from the temporary directory
        relative_path = os.path.basename(base_dir)
        
        # Test deleting the directory
        delete_directory(relative_path)
        
        # Verify directory is deleted
        assert not os.path.exists(base_dir)

def test_delete_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        delete_directory('nonexistent_directory')

def test_delete_file_instead_of_directory():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
        filename = os.path.basename(temp_file_path)
    
    with pytest.raises(NotADirectoryError):
        delete_directory(filename)
    
    # Clean up
    os.unlink(temp_file_path)

def test_invalid_input_type():
    with pytest.raises(TypeError):
        delete_directory(123)  # Non-string input

def test_nested_directory_deletion():
    with tempfile.TemporaryDirectory() as base_dir:
        # Create a nested directory structure
        nested_dir = os.path.join(base_dir, 'level1', 'level2', 'level3')
        os.makedirs(nested_dir)
        
        # Create some files in the nested directory
        with open(os.path.join(nested_dir, 'file.txt'), 'w') as f:
            f.write('test')
        
        # Use relative path
        relative_path = os.path.join(os.path.basename(base_dir), 'level1')
        
        # Delete the middle directory, which should remove everything below it
        delete_directory(relative_path)
        
        # Verify entire nested structure is deleted
        assert not os.path.exists(os.path.join(base_dir, 'level1'))