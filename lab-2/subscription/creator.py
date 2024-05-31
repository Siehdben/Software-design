from subscription import DomesticSubscription, EducationalSubscription, PremiumSubscription

class SubscriptionCreator:
    def create_subscription(self):
        raise NotImplementedError

class WebSite(SubscriptionCreator):
    def create_subscription(self, subscription_type):
        if subscription_type == "domestic":
            return DomesticSubscription()
        elif subscription_type == "educational":
            return EducationalSubscription()
        elif subscription_type == "premium":
            return PremiumSubscription()
        else:
            raise ValueError("Unknown subscription type")

class MobileApp(SubscriptionCreator):
    def create_subscription(self, subscription_type):
        if subscription_type == "domestic":
            return DomesticSubscription()
        elif subscription_type == "educational":
            return EducationalSubscription()
        elif subscription_type == "premium":
            return PremiumSubscription()
        else:
            raise ValueError("Unknown subscription type")

class ManagerCall(SubscriptionCreator):
    def create_subscription(self, subscription_type):
        if subscription_type == "domestic":
            return DomesticSubscription()
        elif subscription_type == "educational":
            return EducationalSubscription()
        elif subscription_type == "premium":
            return PremiumSubscription()
        else:
            raise ValueError("Unknown subscription type")
