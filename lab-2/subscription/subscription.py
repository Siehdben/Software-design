class Subscription:
    def __init__(self, monthly_fee, min_period, channels):
        self.monthly_fee = monthly_fee
        self.min_period = min_period
        self.channels = channels

    def __str__(self):
        return f"Subscription(monthly_fee={self.monthly_fee}, min_period={self.min_period}, channels={self.channels})"

class DomesticSubscription(Subscription):
    def __init__(self):
        super().__init__(monthly_fee=20, min_period=6, channels=["News", "Sports", "Entertainment"])

class EducationalSubscription(Subscription):
    def __init__(self):
        super().__init__(monthly_fee=15, min_period=12, channels=["Science", "History", "Kids"])

class PremiumSubscription(Subscription):
    def __init__(self):
        super().__init__(monthly_fee=50, min_period=3, channels=["All channels", "Exclusive Content", "4K Movies"])
