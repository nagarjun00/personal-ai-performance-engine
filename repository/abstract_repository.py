from abc import ABC, abstractmethod


class AbstractSkillRepository(ABC):

    @abstractmethod
    def get_skill(self, name: str):
        pass

    @abstractmethod
    def save_skill(self, skill):
        pass

    @abstractmethod
    def list_skills(self):
        pass

    # NEW METHODS

    @abstractmethod
    def save_session(self, session):
        pass

    @abstractmethod
    def list_sessions(self):
        pass

    @abstractmethod
    def get_sessions_by_skill(self, skill_name: str):
        pass
