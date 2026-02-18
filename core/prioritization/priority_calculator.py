from core.contracts.priority_contract import BasePriorityCalculator


class PriorityCalculator(BasePriorityCalculator):

    def calculate_priority(self, skill) -> float:
        return (100 - skill.strength) * skill.role_weight
