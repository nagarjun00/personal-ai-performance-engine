from core.models.skill import Skill
from core.prioritization.priority_calculator import PriorityCalculator


def test_priority_calculation():
    skill = Skill(name="Python", strength=40, role_weight=1.5)

    calculator = PriorityCalculator()
    priority = calculator.calculate_priority(skill)

    # (100 - 40) * 1.5 = 60 * 1.5 = 90
    assert priority == 90
