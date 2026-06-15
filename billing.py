"""Lightweight billing helper."""
import logging

logger = logging.getLogger(__name__)


class BillingService:
    def __init__(self, gateway):
        """Create a billing service using the provided payment gateway.

        Args:
            gateway: An object that implements charge() and refund() operations.
        """
        self.gateway = gateway

    def charge_customer(self, customer, amount):
        """Charge a customer the given amount via the payment gateway."""
        token = customer.payment_method.token
        return self.gateway.charge(token, amount)

    def refund(self, transaction_id):
        """Refund a previously charged transaction.

        Raises:
            Exception: Propagates any gateway exception so callers can handle or retry.
        """
        try:
            return self.gateway.refund(transaction_id)
        except Exception:
            logger.exception("Refund failed for transaction_id=%s", transaction_id)
            raise
