from repository.abstract_repository import AbstractSkillRepository


class InMemorySkillRepository(AbstractSkillRepository):

    def __init__(self):
        self._skills = {}
        self._sessions = []  # Global session store

    # Skill methods

    def get_skill(self, name: str):
        return self._skills.get(name)

    def save_skill(self, skill):
        self._skills[skill.name] = skill

    def list_skills(self):
        return list(self._skills.values())

    # Session methods

    def save_session(self, session):
        self._sessions.append(session)

    def list_sessions(self):
        return list(self._sessions)

    def get_sessions_by_skill(self, skill_name: str):
        return [
            session for session in self._sessions
            if session.skill_name == skill_name
        ]
