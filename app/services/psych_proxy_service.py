from app.configs.configs import Configs
from app.configs.system_modes import SystemModes
from app.psych_proxy.baseline_engine import BaselineEngine
from app.twins.psych_proxy_twin import PsychologicalProxyTwin

baseline_engine = BaselineEngine()
psych_twin = PsychologicalProxyTwin()
configs = Configs()

# Get user psychological history
USER_HISTORY = {}

def run_psycho_twin(user_id: str, session: dict):

    # check if user exists and initialize a new user dict
    if user_id not in USER_HISTORY:
        USER_HISTORY[user_id] = []

    USER_HISTORY[user_id].append(session)

    # construct minimum history to build a baseline
    if len(USER_HISTORY[user_id]) < configs.MIN_SESSIONS:
        signal = USER_HISTORY[user_id]
        baseline_engine.update_user_profiles(user_id, signal)
        return {
            "sub_twin": "psych_proxy",
            "user_id": user_id,
            "risk_score": 0.0,
            "signals": {},
            "interpretation": "Learning User Behavior Baseline",
            "mode": SystemModes.ACTIVE.value
        }

    # Build a baseline
    history = USER_HISTORY[user_id][:-1] #All history except the current
    baseline = baseline_engine.update_user_profiles(user_id, history)

    # Run the twin to do evaluation
    result = psych_twin.evaluate_user_session(session, baseline)

    return result

