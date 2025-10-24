"""
Unit tests for melat.py - GigMarket Utilities
"""

import pytest
from datetime import datetime
from melat import (
    Transaction, Currency, GigStatus, CurrencyConverter,
    ReputationScore, MarketplaceAnalytics, generate_transaction_id,
    calculate_escrow_release_schedule, search_gigs_by_price_range,
    get_status_emoji
)


class TestTransaction:
    """Test Transaction class"""
    
    def test_transaction_creation(self):
        """Test creating a basic transaction"""
        txn = Transaction(
            transaction_id="TEST123",
            buyer_id="buyer1",
            seller_id="seller1",
            amount=100.0,
            currency=Currency.USD
        )
        
        assert txn.transaction_id == "TEST123"
        assert txn.buyer_id == "buyer1"
        assert txn.seller_id == "seller1"
        assert txn.amount == 100.0
        assert txn.currency == Currency.USD
        assert txn.status == GigStatus.PENDING
    
    def test_calculate_fee(self):
        """Test platform fee calculation"""
        txn = Transaction(
            transaction_id="TEST123",
            buyer_id="buyer1",
            seller_id="seller1",
            amount=100.0,
            currency=Currency.USD
        )
        
        # Default 15% fee
        assert txn.calculate_fee() == 15.0
        
        # Custom 10% fee
        assert txn.calculate_fee(0.10) == 10.0
    
    def test_seller_payout(self):
        """Test seller payout calculation"""
        txn = Transaction(
            transaction_id="TEST123",
            buyer_id="buyer1",
            seller_id="seller1",
            amount=100.0,
            currency=Currency.USD
        )
        
        # With 15% fee, seller gets 85
        assert txn.seller_payout() == 85.0
        
        # With 10% fee, seller gets 90
        assert txn.seller_payout(0.10) == 90.0
    
    def test_to_dict(self):
        """Test converting transaction to dictionary"""
        txn = Transaction(
            transaction_id="TEST123",
            buyer_id="buyer1",
            seller_id="seller1",
            amount=100.0,
            currency=Currency.USD
        )
        
        txn_dict = txn.to_dict()
        
        assert txn_dict["transaction_id"] == "TEST123"
        assert txn_dict["buyer_id"] == "buyer1"
        assert txn_dict["seller_id"] == "seller1"
        assert txn_dict["amount"] == 100.0
        assert txn_dict["currency"] == "USD"
        assert txn_dict["status"] == "pending"
        assert "timestamp" in txn_dict


class TestCurrencyConverter:
    """Test CurrencyConverter class"""
    
    def test_same_currency_conversion(self):
        """Test converting between same currency"""
        result = CurrencyConverter.convert(100, Currency.USD, Currency.USD)
        assert result == 100.0
    
    def test_usd_to_eur_conversion(self):
        """Test USD to EUR conversion"""
        result = CurrencyConverter.convert(100, Currency.USD, Currency.EUR)
        assert result == 92.0
    
    def test_usd_to_gbp_conversion(self):
        """Test USD to GBP conversion"""
        result = CurrencyConverter.convert(100, Currency.USD, Currency.GBP)
        assert result == 79.0
    
    def test_eur_to_usd_conversion(self):
        """Test EUR to USD conversion"""
        result = CurrencyConverter.convert(92, Currency.EUR, Currency.USD)
        assert result == 100.0
    
    def test_gbp_to_eur_conversion(self):
        """Test GBP to EUR conversion (through USD)"""
        result = CurrencyConverter.convert(79, Currency.GBP, Currency.EUR)
        # 79 GBP -> 100 USD -> 92 EUR
        assert result == 92.0


class TestReputationScore:
    """Test ReputationScore class"""
    
    def test_initial_reputation(self):
        """Test initial reputation state"""
        rep = ReputationScore(user_id="user123")
        
        assert rep.user_id == "user123"
        assert rep.total_ratings == 0
        assert rep.average_rating == 0.0
        assert rep.completed_gigs == 0
        assert rep.on_time_delivery_rate == 100.0
    
    def test_add_single_rating(self):
        """Test adding a single rating"""
        rep = ReputationScore(user_id="user123")
        rep.add_rating(4.5)
        
        assert rep.total_ratings == 1
        assert rep.average_rating == 4.5
    
    def test_add_multiple_ratings(self):
        """Test adding multiple ratings and calculating average"""
        rep = ReputationScore(user_id="user123")
        rep.add_rating(5.0)
        rep.add_rating(4.0)
        rep.add_rating(3.0)
        
        assert rep.total_ratings == 3
        assert rep.average_rating == 4.0
    
    def test_invalid_rating(self):
        """Test that invalid ratings raise ValueError"""
        rep = ReputationScore(user_id="user123")
        
        with pytest.raises(ValueError):
            rep.add_rating(6.0)
        
        with pytest.raises(ValueError):
            rep.add_rating(-1.0)
    
    def test_complete_gig_on_time(self):
        """Test completing a gig on time"""
        rep = ReputationScore(user_id="user123")
        rep.complete_gig(on_time=True)
        
        assert rep.completed_gigs == 1
        assert rep.on_time_delivery_rate == 100.0
    
    def test_complete_gig_late(self):
        """Test completing a gig late"""
        rep = ReputationScore(user_id="user123")
        rep.complete_gig(on_time=True)
        rep.complete_gig(on_time=False)
        
        assert rep.completed_gigs == 2
        assert rep.on_time_delivery_rate == 50.0
    
    def test_newcomer_badge(self):
        """Test newcomer badge for users with < 5 gigs"""
        rep = ReputationScore(user_id="user123")
        rep.add_rating(5.0)
        rep.complete_gig(on_time=True)
        
        assert rep.get_badge() == "🌱 Newcomer"
    
    def test_elite_badge(self):
        """Test elite badge criteria"""
        rep = ReputationScore(user_id="user123")
        
        # Add 5 perfect ratings
        for _ in range(5):
            rep.add_rating(5.0)
            rep.complete_gig(on_time=True)
        
        assert rep.completed_gigs >= 5
        assert rep.average_rating >= 4.8
        assert rep.on_time_delivery_rate >= 95
        assert rep.get_badge() == "⭐ Elite"
    
    def test_pro_badge(self):
        """Test pro badge criteria"""
        rep = ReputationScore(user_id="user123")
        
        # Add ratings averaging 4.5
        for _ in range(5):
            rep.add_rating(4.5)
            rep.complete_gig(on_time=True)
        
        assert rep.get_badge() in ["⭐ Elite", "💎 Pro"]


class TestMarketplaceAnalytics:
    """Test MarketplaceAnalytics class"""
    
    def test_empty_analytics(self):
        """Test analytics with no transactions"""
        analytics = MarketplaceAnalytics()
        
        assert analytics.total_volume() == 0.0
        assert analytics.average_transaction_value() == 0.0
        assert analytics.completion_rate() == 0.0
    
    def test_add_transaction(self):
        """Test adding transactions"""
        analytics = MarketplaceAnalytics()
        
        txn = Transaction(
            transaction_id="TEST123",
            buyer_id="buyer1",
            seller_id="seller1",
            amount=100.0,
            currency=Currency.USD
        )
        
        analytics.add_transaction(txn)
        assert len(analytics.transactions) == 1
    
    def test_total_volume(self):
        """Test calculating total transaction volume"""
        analytics = MarketplaceAnalytics()
        
        txn1 = Transaction(
            transaction_id="TEST1",
            buyer_id="buyer1",
            seller_id="seller1",
            amount=100.0,
            currency=Currency.USD
        )
        
        txn2 = Transaction(
            transaction_id="TEST2",
            buyer_id="buyer2",
            seller_id="seller2",
            amount=200.0,
            currency=Currency.USD
        )
        
        analytics.add_transaction(txn1)
        analytics.add_transaction(txn2)
        
        assert analytics.total_volume() == 300.0
    
    def test_average_transaction_value(self):
        """Test calculating average transaction value"""
        analytics = MarketplaceAnalytics()
        
        for i in range(5):
            txn = Transaction(
                transaction_id=f"TEST{i}",
                buyer_id="buyer1",
                seller_id="seller1",
                amount=100.0,
                currency=Currency.USD
            )
            analytics.add_transaction(txn)
        
        assert analytics.average_transaction_value() == 100.0
    
    def test_completion_rate(self):
        """Test calculating completion rate"""
        analytics = MarketplaceAnalytics()
        
        # Add 3 completed and 2 pending transactions
        for i in range(3):
            txn = Transaction(
                transaction_id=f"TEST{i}",
                buyer_id="buyer1",
                seller_id="seller1",
                amount=100.0,
                currency=Currency.USD,
                status=GigStatus.COMPLETED
            )
            analytics.add_transaction(txn)
        
        for i in range(2):
            txn = Transaction(
                transaction_id=f"TEST{i+3}",
                buyer_id="buyer1",
                seller_id="seller1",
                amount=100.0,
                currency=Currency.USD,
                status=GigStatus.PENDING
            )
            analytics.add_transaction(txn)
        
        assert analytics.completion_rate() == 60.0


class TestUtilityFunctions:
    """Test utility functions"""
    
    def test_generate_transaction_id(self):
        """Test transaction ID generation"""
        txn_id = generate_transaction_id("buyer1", "seller1")
        
        assert isinstance(txn_id, str)
        assert len(txn_id) == 16
        assert txn_id.isupper()
    
    def test_transaction_id_uniqueness(self):
        """Test that transaction IDs are unique"""
        txn_id1 = generate_transaction_id("buyer1", "seller1")
        txn_id2 = generate_transaction_id("buyer1", "seller1")
        
        # Should be different due to different timestamps
        assert txn_id1 != txn_id2
    
    def test_calculate_escrow_release_schedule(self):
        """Test escrow payment schedule calculation"""
        schedule = calculate_escrow_release_schedule(1000.0, 4)
        
        assert len(schedule) == 4
        assert sum(schedule) == 1000.0
        assert all(amount > 0 for amount in schedule)
    
    def test_escrow_schedule_single_milestone(self):
        """Test escrow schedule with single milestone"""
        schedule = calculate_escrow_release_schedule(100.0, 1)
        
        assert len(schedule) == 1
        assert schedule[0] == 100.0
    
    def test_escrow_schedule_invalid_milestones(self):
        """Test escrow schedule with invalid milestones"""
        with pytest.raises(ValueError):
            calculate_escrow_release_schedule(100.0, 0)
        
        with pytest.raises(ValueError):
            calculate_escrow_release_schedule(100.0, -1)
    
    def test_search_gigs_by_price_range(self):
        """Test searching gigs by price range"""
        gigs = [
            {"id": 1, "price": 50, "currency": "USD"},
            {"id": 2, "price": 150, "currency": "USD"},
            {"id": 3, "price": 250, "currency": "USD"},
            {"id": 4, "price": 75, "currency": "USD"},
        ]
        
        results = search_gigs_by_price_range(gigs, 50, 100)
        
        assert len(results) == 2
        assert results[0]["id"] == 1
        assert results[1]["id"] == 4
    
    def test_search_gigs_empty_list(self):
        """Test searching empty gig list"""
        results = search_gigs_by_price_range([], 50, 100)
        assert len(results) == 0
    
    def test_get_status_emoji(self):
        """Test emoji status representation"""
        assert get_status_emoji(GigStatus.PENDING) == "⏳"
        assert get_status_emoji(GigStatus.IN_PROGRESS) == "🚀"
        assert get_status_emoji(GigStatus.COMPLETED) == "✅"
        assert get_status_emoji(GigStatus.CANCELLED) == "❌"


class TestIntegration:
    """Integration tests combining multiple features"""
    
    def test_full_transaction_workflow(self):
        """Test complete transaction workflow with analytics"""
        analytics = MarketplaceAnalytics()
        
        # Create transaction
        txn_id = generate_transaction_id("buyer1", "seller1")
        txn = Transaction(
            transaction_id=txn_id,
            buyer_id="buyer1",
            seller_id="seller1",
            amount=100.0,
            currency=Currency.USD,
            status=GigStatus.COMPLETED
        )
        
        # Add to analytics
        analytics.add_transaction(txn)
        
        # Verify
        assert analytics.total_volume() == 100.0
        assert analytics.completion_rate() == 100.0
        assert txn.seller_payout() == 85.0
    
    def test_seller_reputation_tracking(self):
        """Test tracking seller reputation over multiple gigs"""
        rep = ReputationScore(user_id="seller123")
        
        # Complete 5 gigs with ratings
        ratings = [5.0, 4.8, 4.9, 5.0, 4.7]
        for rating in ratings:
            rep.add_rating(rating)
            rep.complete_gig(on_time=True)
        
        assert rep.completed_gigs == 5
        assert rep.average_rating >= 4.8
        assert rep.on_time_delivery_rate == 100.0
        assert rep.get_badge() == "⭐ Elite"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
