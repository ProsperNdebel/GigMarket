"""Validation utilities for user input in GigMarket."""
import re
from typing import Optional


def is_valid_email(email: str) -> bool:
    """Validate email address format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid email format
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def is_valid_phone(phone: str, country_code: str = "US") -> bool:
    """Validate phone number format.
    
    Args:
        phone: Phone number to validate
        country_code: Country code for validation rules
        
    Returns:
        True if valid phone format
    """
    # Remove common separators
    cleaned = re.sub(r'[\s\-\(\)\.]', '', phone)
    
    if country_code == "US":
        # US: 10 digits, optional +1 prefix
        pattern = r'^(\+?1)?[2-9]\d{9}$'
        return bool(re.match(pattern, cleaned))
    
    # Generic: 7-15 digits
    return len(cleaned) >= 7 and len(cleaned) <= 15 and cleaned.isdigit()


def is_strong_password(password: str) -> tuple[bool, list[str]]:
    """Check if password meets strength requirements.
    
    Args:
        password: Password to validate
        
    Returns:
        Tuple of (is_valid, list_of_issues)
    """
    issues = []
    
    if len(password) < 8:
        issues.append("Password must be at least 8 characters long")
    
    if not re.search(r'[A-Z]', password):
        issues.append("Password must contain at least one uppercase letter")
    
    if not re.search(r'[a-z]', password):
        issues.append("Password must contain at least one lowercase letter")
    
    if not re.search(r'\d', password):
        issues.append("Password must contain at least one digit")
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        issues.append("Password must contain at least one special character")
    
    return len(issues) == 0, issues


def is_valid_username(username: str) -> tuple[bool, Optional[str]]:
    """Validate username format.
    
    Args:
        username: Username to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if len(username) < 3:
        return False, "Username must be at least 3 characters long"
    
    if len(username) > 30:
        return False, "Username must be 30 characters or less"
    
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False, "Username can only contain letters, numbers, and underscores"
    
    if username[0].isdigit():
        return False, "Username cannot start with a number"
    
    return True, None


def is_valid_url(url: str) -> bool:
    """Validate URL format.
    
    Args:
        url: URL to validate
        
    Returns:
        True if valid URL format
    """
    pattern = r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$'
    return bool(re.match(pattern, url))


def sanitize_html(text: str) -> str:
    """Remove HTML tags from text for safety.
    
    Args:
        text: Text potentially containing HTML
        
    Returns:
        Text with HTML tags removed
    """
    # Remove HTML tags
    clean = re.sub(r'<[^>]+>', '', text)
    # Remove script tags and content
    clean = re.sub(r'<script[^>]*>.*?</script>', '', clean, flags=re.DOTALL | re.IGNORECASE)
    return clean


def validate_file_extension(filename: str, allowed_extensions: list[str]) -> bool:
    """Validate file has allowed extension.
    
    Args:
        filename: Filename to validate
        allowed_extensions: List of allowed extensions (e.g., ['.jpg', '.png'])
        
    Returns:
        True if file extension is allowed
    """
    extension = filename.lower().split('.')[-1] if '.' in filename else ''
    extension_with_dot = f'.{extension}'
    return extension_with_dot in [ext.lower() for ext in allowed_extensions]
