from datetime import date
from core.contracts.scorer_contract import BaseScorer
from core.contracts.decay_contract import BaseDecayPolicy
from core.contracts.priority_contract import BasePriorityCalculator


class SkillEngine:

    def __init__(
        self,
        repository,
        scorer: BaseScorer,
        decay_policy: BaseDecayPolicy,
        priority_calculator: BasePriorityCalculator,
    ):
        self.repository = repository
        self.scorer = scorer
        self.decay_policy = decay_policy
        self.priority_calculator = priority_calculator

    def process_session(self, session):
        skill = self.repository.get_skill(session.skill_name)

        if skill is None:
            raise ValueError(f"Skill '{session.skill_name}' not found.")

        delta = self.scorer.calculate_delta(session)

        skill.update_strength(delta)
        skill.last_practiced = session.session_date

        self.repository.save_skill(skill)

        # NEW: store session globally
        self.repository.save_session(session)

    def apply_decay_to_all(self, current_date: date):
        for skill in self.repository.list_skills():
            multiplier = self.decay_policy.compute_decay_multiplier(
                skill.last_practiced,
                current_date
            )

            skill.apply_decay(multiplier)
            self.repository.save_skill(skill)

    def get_daily_focus(self):
        skills = self.repository.list_skills()

        if not skills:
            return None

        return max(
            skills,
            key=lambda skill: self.priority_calculator.calculate_priority(skill)
        )
