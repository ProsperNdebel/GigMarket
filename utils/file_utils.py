"""File processing utilities for GigMarket."""
import os
import hashlib
from typing import Optional
from pathlib import Path


def get_file_size_mb(file_path: str) -> float:
    """Get file size in megabytes.
    
    Args:
        file_path: Path to file
        
    Returns:
        File size in MB
    """
    size_bytes = os.path.getsize(file_path)
    return size_bytes / (1024 * 1024)


def calculate_file_hash(file_path: str, algorithm: str = 'sha256') -> str:
    """Calculate hash of file contents.
    
    Args:
        file_path: Path to file
        algorithm: Hash algorithm (md5, sha1, sha256)
        
    Returns:
        Hexadecimal hash string
    """
    hash_func = hashlib.new(algorithm)
    
    with open(file_path, 'rb') as f:
        # Read in chunks to handle large files
        for chunk in iter(lambda: f.read(4096), b''):
            hash_func.update(chunk)
    
    return hash_func.hexdigest()


def ensure_directory_exists(directory_path: str) -> None:
    """Create directory if it doesn't exist.
    
    Args:
        directory_path: Path to directory
    """
    Path(directory_path).mkdir(parents=True, exist_ok=True)


def get_file_extension(filename: str) -> str:
    """Extract file extension from filename.
    
    Args:
        filename: Filename or path
        
    Returns:
        File extension with dot (e.g., '.jpg')
    """
    return os.path.splitext(filename)[1].lower()


def generate_unique_filename(original_filename: str, prefix: Optional[str] = None) -> str:
    """Generate unique filename using timestamp and hash.
    
    Args:
        original_filename: Original filename
        prefix: Optional prefix for filename
        
    Returns:
        Unique filename
    """
    import time
    import uuid
    
    extension = get_file_extension(original_filename)
    unique_id = str(uuid.uuid4())[:8]
    timestamp = str(int(time.time()))
    
    if prefix:
        return f"{prefix}_{timestamp}_{unique_id}{extension}"
    return f"{timestamp}_{unique_id}{extension}"


def is_file_type(filename: str, file_type: str) -> bool:
    """Check if file is of specific type.
    
    Args:
        filename: Filename to check
        file_type: Type to check ('image', 'video', 'document', 'audio')
        
    Returns:
        True if file matches type
    """
    extension = get_file_extension(filename)
    
    type_mappings = {
        'image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg'],
        'video': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm'],
        'document': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
        'audio': ['.mp3', '.wav', '.ogg', '.m4a', '.flac', '.aac']
    }
    
    return extension in type_mappings.get(file_type, [])


def clean_filename(filename: str) -> str:
    """Clean filename by removing/replacing invalid characters.
    
    Args:
        filename: Filename to clean
        
    Returns:
        Cleaned filename
    """
    # Remove or replace invalid characters
    invalid_chars = '<>:"\/|?*'
    cleaned = filename
    
    for char in invalid_chars:
        cleaned = cleaned.replace(char, '_')
    
    # Remove leading/trailing spaces and dots
    cleaned = cleaned.strip('. ')
    
    return cleaned
