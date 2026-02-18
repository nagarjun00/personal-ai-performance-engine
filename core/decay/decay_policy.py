from datetime import date
from core.contracts.decay_contract import BaseDecayPolicy


class DecayPolicy(BaseDecayPolicy):

    DAILY_DECAY_MULTIPLIER = 0.995
    GRACE_PERIOD_DAYS = 7

    @staticmethod
    def compute_decay_multiplier(
        last_practiced: date,
        current_date: date
    ) -> float:
        if last_practiced is None:
            return 1.0

        inactive_days = (current_date - last_practiced).days

        if inactive_days <= DecayPolicy.GRACE_PERIOD_DAYS:
            return 1.0

        decay_days = inactive_days - DecayPolicy.GRACE_PERIOD_DAYS

        return DecayPolicy.DAILY_DECAY_MULTIPLIER ** decay_days
