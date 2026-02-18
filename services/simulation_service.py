class SimulationService:

    def __init__(self, engine):
        self.engine = engine

    def run_sessions(self, sessions):
        for session in sessions:
            self.engine.process_session(session)
