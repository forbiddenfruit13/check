"""Lightweight billing helper."""
import logging

logger = logging.getLogger(__name__)


class BillingService:
    def __init__(self, gateway):
        self.gateway = gateway

    def charge_customer(self, customer, amount):
        """Charge a customer the given amount via the payment gateway."""
        token = customer.payment_method.token
        return self.gateway.charge(token, amount)

    def refund(self, transaction_id):
        """Refund a previously charged transaction."""
        try:
            return self.gateway.refund(transaction_id)
        except Exception:
            logger.exception("Refund failed for transaction %s", transaction_id)
            raise
