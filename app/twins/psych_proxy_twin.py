from app.configs.system_modes import SystemModes
from app.utils.risk_engine import RiskEngine
from app.utils.risk_interpretation import RiskInterpretation
from app.utils.signals_calculator import calculate_time_deviation, calculate_amount_deviation, \
    calculate_recipient_familiarity, calculate_speed_deviation

risk_engine = RiskEngine()
risk_interpretation = RiskInterpretation()

class PsychologicalProxyTwin:

    def evaluate_user_session(self, session: dict, baseline: dict):

        # extract signals
        signals = {
            "time_deviation": calculate_time_deviation(session, baseline),
            "amount_deviation": calculate_amount_deviation(session, baseline),
            "recipient_familiarity": calculate_recipient_familiarity(session, baseline),
            "speed_deviation": calculate_speed_deviation(session, baseline)
        }

        # Risk scoring
        risk_score = risk_engine.compute_risk(signals)

        # Interpret Risk
        interpretation = risk_interpretation.classify_psychological_intent(risk_score)

        return {
            "sub_twin": "psych_proxy",
            "user_id": session.get("user_id"),
            "risk_score": round(risk_score, 2),
            "signals": signals,
            "interpretation": interpretation,
            "mode": SystemModes.LEARNING.value,
        }

