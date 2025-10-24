"""
Melat - A Cool Utility Module for GigMarket
============================================

This module provides utilities for managing gig marketplace transactions,
including price calculations, currency conversions, and reputation management.

Author: AI Assistant
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum
import hashlib
import json


class Currency(Enum):
    """Supported currencies in the marketplace"""
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    ETB = "ETB"  # Ethiopian Birr


class GigStatus(Enum):
    """Status of a gig"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


@dataclass
class Transaction:
    """Represents a transaction in the gig marketplace"""
    transaction_id: str
    buyer_id: str
    seller_id: str
    amount: float
    currency: Currency
    timestamp: datetime = field(default_factory=datetime.now)
    status: GigStatus = GigStatus.PENDING
    
    def to_dict(self) -> Dict:
        """Convert transaction to dictionary"""
        return {
            "transaction_id": self.transaction_id,
            "buyer_id": self.buyer_id,
            "seller_id": self.seller_id,
            "amount": self.amount,
            "currency": self.currency.value,
            "timestamp": self.timestamp.isoformat(),
            "status": self.status.value
        }
    
    def calculate_fee(self, fee_percentage: float = 0.15) -> float:
        """Calculate platform fee (default 15%)"""
        return round(self.amount * fee_percentage, 2)
    
    def seller_payout(self, fee_percentage: float = 0.15) -> float:
        """Calculate seller payout after fees"""
        return round(self.amount - self.calculate_fee(fee_percentage), 2)


class CurrencyConverter:
    """Currency converter with exchange rates"""
    
    # Exchange rates relative to USD
    EXCHANGE_RATES = {
        Currency.USD: 1.0,
        Currency.EUR: 0.92,
        Currency.GBP: 0.79,
        Currency.ETB: 56.50
    }
    
    @classmethod
    def convert(cls, amount: float, from_currency: Currency, to_currency: Currency) -> float:
        """Convert amount from one currency to another"""
        if from_currency == to_currency:
            return amount
        
        # Convert to USD first, then to target currency
        usd_amount = amount / cls.EXCHANGE_RATES[from_currency]
        target_amount = usd_amount * cls.EXCHANGE_RATES[to_currency]
        
        return round(target_amount, 2)


@dataclass
class ReputationScore:
    """User reputation management system"""
    user_id: str
    total_ratings: int = 0
    average_rating: float = 0.0
    completed_gigs: int = 0
    on_time_delivery_rate: float = 100.0
    
    def add_rating(self, rating: float) -> None:
        """Add a new rating and update average"""
        if not 0 <= rating <= 5:
            raise ValueError("Rating must be between 0 and 5")
        
        total_score = self.average_rating * self.total_ratings
        self.total_ratings += 1
        self.average_rating = round((total_score + rating) / self.total_ratings, 2)
    
    def complete_gig(self, on_time: bool = True) -> None:
        """Mark a gig as completed and update delivery rate"""
        self.completed_gigs += 1
        if on_time:
            # Recalculate on-time delivery rate
            on_time_count = round(self.on_time_delivery_rate / 100 * (self.completed_gigs - 1))
            self.on_time_delivery_rate = round(
                (on_time_count + 1) / self.completed_gigs * 100, 2
            )
        else:
            on_time_count = round(self.on_time_delivery_rate / 100 * (self.completed_gigs - 1))
            self.on_time_delivery_rate = round(
                on_time_count / self.completed_gigs * 100, 2
            )
    
    def get_badge(self) -> str:
        """Get reputation badge based on performance"""
        if self.completed_gigs < 5:
            return "🌱 Newcomer"
        elif self.average_rating >= 4.8 and self.on_time_delivery_rate >= 95:
            return "⭐ Elite"
        elif self.average_rating >= 4.5 and self.on_time_delivery_rate >= 90:
            return "💎 Pro"
        elif self.average_rating >= 4.0 and self.on_time_delivery_rate >= 85:
            return "🎯 Veteran"
        else:
            return "✅ Standard"


class MarketplaceAnalytics:
    """Analytics utilities for the marketplace"""
    
    def __init__(self):
        self.transactions: List[Transaction] = []
    
    def add_transaction(self, transaction: Transaction) -> None:
        """Add a transaction to analytics"""
        self.transactions.append(transaction)
    
    def total_volume(self, currency: Currency = Currency.USD) -> float:
        """Calculate total transaction volume in specified currency"""
        total = 0.0
        for txn in self.transactions:
            converted = CurrencyConverter.convert(
                txn.amount, txn.currency, currency
            )
            total += converted
        return round(total, 2)
    
    def average_transaction_value(self, currency: Currency = Currency.USD) -> float:
        """Calculate average transaction value"""
        if not self.transactions:
            return 0.0
        return round(self.total_volume(currency) / len(self.transactions), 2)
    
    def completion_rate(self) -> float:
        """Calculate percentage of completed transactions"""
        if not self.transactions:
            return 0.0
        
        completed = sum(
            1 for txn in self.transactions 
            if txn.status == GigStatus.COMPLETED
        )
        return round(completed / len(self.transactions) * 100, 2)


def generate_transaction_id(buyer_id: str, seller_id: str, timestamp: Optional[datetime] = None) -> str:
    """Generate a unique transaction ID using hash"""
    if timestamp is None:
        timestamp = datetime.now()
    
    data = f"{buyer_id}:{seller_id}:{timestamp.isoformat()}"
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()[:16].upper()


def calculate_escrow_release_schedule(total_amount: float, milestones: int) -> List[float]:
    """Calculate escrow release amounts for milestone-based payments"""
    if milestones <= 0:
        raise ValueError("Milestones must be positive")
    
    base_amount = total_amount / milestones
    schedule = [round(base_amount, 2) for _ in range(milestones - 1)]
    
    # Last payment includes any rounding difference
    last_payment = round(total_amount - sum(schedule), 2)
    schedule.append(last_payment)
    
    return schedule


def search_gigs_by_price_range(
    gigs: List[Dict], 
    min_price: float, 
    max_price: float,
    currency: Currency = Currency.USD
) -> List[Dict]:
    """Search gigs within a price range"""
    filtered_gigs = []
    
    for gig in gigs:
        gig_price = gig.get("price", 0)
        gig_currency = Currency(gig.get("currency", "USD"))
        
        # Convert to target currency for comparison
        converted_price = CurrencyConverter.convert(gig_price, gig_currency, currency)
        
        if min_price <= converted_price <= max_price:
            filtered_gigs.append(gig)
    
    return filtered_gigs


# Cool bonus feature: Emoji-based status reporter
def get_status_emoji(status: GigStatus) -> str:
    """Get emoji representation of gig status"""
    emoji_map = {
        GigStatus.PENDING: "⏳",
        GigStatus.IN_PROGRESS: "🚀",
        GigStatus.COMPLETED: "✅",
        GigStatus.CANCELLED: "❌"
    }
    return emoji_map.get(status, "❓")


if __name__ == "__main__":
    # Demo usage
    print("🎉 Melat - GigMarket Utilities Demo\n")
    
    # Create a transaction
    txn_id = generate_transaction_id("buyer123", "seller456")
    txn = Transaction(
        transaction_id=txn_id,
        buyer_id="buyer123",
        seller_id="seller456",
        amount=100.0,
        currency=Currency.USD
    )
    
    print(f"Transaction ID: {txn.transaction_id}")
    print(f"Amount: {txn.amount} {txn.currency.value}")
    print(f"Platform Fee: ${txn.calculate_fee()}")
    print(f"Seller Payout: ${txn.seller_payout()}\n")
    
    # Currency conversion
    eur_amount = CurrencyConverter.convert(100, Currency.USD, Currency.EUR)
    print(f"$100 USD = €{eur_amount} EUR\n")
    
    # Reputation system
    rep = ReputationScore(user_id="seller456")
    rep.add_rating(5.0)
    rep.add_rating(4.8)
    rep.complete_gig(on_time=True)
    print(f"Seller Badge: {rep.get_badge()}")
    print(f"Average Rating: {rep.average_rating} ⭐")
    print(f"On-time Delivery: {rep.on_time_delivery_rate}%")
