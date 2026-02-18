class RoleProfile:
    def __init__(self, role_name: str, skill_weights: dict[str, float]):
        self.role_name = role_name
        self.skill_weights = skill_weights
