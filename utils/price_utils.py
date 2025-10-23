"""Price calculation utilities for GigMarket."""
from decimal import Decimal, ROUND_HALF_UP
from typing import Optional


def calculate_platform_fee(amount: Decimal, fee_percentage: Decimal = Decimal('0.15')) -> Decimal:
    """Calculate platform service fee.
    
    Args:
        amount: Transaction amount
        fee_percentage: Fee percentage (default 15%)
        
    Returns:
        Platform fee amount
    """
    fee = amount * fee_percentage
    return fee.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def calculate_seller_earnings(amount: Decimal, fee_percentage: Decimal = Decimal('0.15')) -> Decimal:
    """Calculate seller earnings after platform fee.
    
    Args:
        amount: Total transaction amount
        fee_percentage: Platform fee percentage
        
    Returns:
        Amount seller receives
    """
    platform_fee = calculate_platform_fee(amount, fee_percentage)
    return amount - platform_fee


def apply_discount(price: Decimal, discount_percentage: Decimal) -> Decimal:
    """Apply discount percentage to price.
    
    Args:
        price: Original price
        discount_percentage: Discount percentage (e.g., 20 for 20%)
        
    Returns:
        Discounted price
    """
    discount_amount = price * (discount_percentage / Decimal('100'))
    final_price = price - discount_amount
    return final_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def format_currency(amount: Decimal, currency: str = "USD", symbol: str = "$") -> str:
    """Format amount as currency string.
    
    Args:
        amount: Amount to format
        currency: Currency code
        symbol: Currency symbol
        
    Returns:
        Formatted currency string
    """
    formatted_amount = f"{amount:,.2f}"
    return f"{symbol}{formatted_amount} {currency}"


def calculate_bulk_discount(quantity: int, unit_price: Decimal) -> Decimal:
    """Calculate price with bulk discount tiers.
    
    Args:
        quantity: Number of items
        unit_price: Price per item
        
    Returns:
        Total price with bulk discount applied
    """
    total = quantity * unit_price
    
    # Apply tiered discounts
    if quantity >= 100:
        discount = Decimal('0.20')  # 20% off
    elif quantity >= 50:
        discount = Decimal('0.15')  # 15% off
    elif quantity >= 20:
        discount = Decimal('0.10')  # 10% off
    elif quantity >= 10:
        discount = Decimal('0.05')  # 5% off
    else:
        discount = Decimal('0.00')
    
    discounted_total = total * (Decimal('1.00') - discount)
    return discounted_total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def split_payment(total_amount: Decimal, num_splits: int) -> list[Decimal]:
    """Split payment into equal parts.
    
    Args:
        total_amount: Total amount to split
        num_splits: Number of splits
        
    Returns:
        List of split amounts
    """
    if num_splits <= 0:
        raise ValueError("Number of splits must be positive")
    
    base_amount = (total_amount / num_splits).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    splits = [base_amount] * num_splits
    
    # Adjust for rounding differences
    total_splits = sum(splits)
    difference = total_amount - total_splits
    
    if difference != 0:
        splits[-1] += difference
    
    return splits
