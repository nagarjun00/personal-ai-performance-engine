from datetime import date, timedelta
from core.decay.decay_policy import DecayPolicy


def test_no_decay_within_grace():
    today = date.today()
    last = today - timedelta(days=5)

    multiplier = DecayPolicy.compute_decay_multiplier(last, today)
    assert multiplier == 1.0


def test_decay_after_grace():
    today = date.today()
    last = today - timedelta(days=10)

    # 10 days inactive
    # 7 grace → 3 decay days
    expected = 0.995 ** 3

    multiplier = DecayPolicy.compute_decay_multiplier(last, today)

    assert round(multiplier, 6) == round(expected, 6)

