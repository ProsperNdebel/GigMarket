"""DateTime utility functions for GigMarket scheduling."""
from datetime import datetime, timedelta
from typing import Optional
import calendar


def is_business_day(date: datetime) -> bool:
    """Check if given date is a business day (Monday-Friday).
    
    Args:
        date: Date to check
        
    Returns:
        True if business day, False otherwise
    """
    return date.weekday() < 5


def get_next_business_day(date: Optional[datetime] = None) -> datetime:
    """Get the next business day from given date.
    
    Args:
        date: Starting date (defaults to today)
        
    Returns:
        Next business day
    """
    if date is None:
        date = datetime.now()
    
    next_day = date + timedelta(days=1)
    while not is_business_day(next_day):
        next_day += timedelta(days=1)
    
    return next_day


def format_time_ago(timestamp: datetime) -> str:
    """Format timestamp as human-readable time ago string.
    
    Args:
        timestamp: Timestamp to format
        
    Returns:
        Human-readable string (e.g., '2 hours ago')
    """
    now = datetime.now()
    diff = now - timestamp
    
    seconds = diff.total_seconds()
    
    if seconds < 60:
        return "just now"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    elif seconds < 86400:
        hours = int(seconds / 3600)
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    elif seconds < 604800:
        days = int(seconds / 86400)
        return f"{days} day{'s' if days != 1 else ''} ago"
    else:
        weeks = int(seconds / 604800)
        return f"{weeks} week{'s' if weeks != 1 else ''} ago"


def get_month_date_range(year: int, month: int) -> tuple[datetime, datetime]:
    """Get start and end datetime for a given month.
    
    Args:
        year: Year
        month: Month (1-12)
        
    Returns:
        Tuple of (start_date, end_date)
    """
    start_date = datetime(year, month, 1)
    last_day = calendar.monthrange(year, month)[1]
    end_date = datetime(year, month, last_day, 23, 59, 59)
    
    return start_date, end_date


def calculate_deadline(start_date: datetime, business_days: int) -> datetime:
    """Calculate deadline date adding business days.
    
    Args:
        start_date: Starting date
        business_days: Number of business days to add
        
    Returns:
        Deadline date
    """
    current_date = start_date
    days_added = 0
    
    while days_added < business_days:
        current_date += timedelta(days=1)
        if is_business_day(current_date):
            days_added += 1
    
    return current_date
