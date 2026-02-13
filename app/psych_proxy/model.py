from .baseline import get_baseline
from .signals import extract_signals
from .scorer import psych_risk


def run_psych_proxy(user_id, session):
    baseline = get_baseline(user_id)
    signals = extract_signals(session)
    risk = psych_risk(signals, baseline)

    return {
        "sub_twin": "psych_proxy",
        "user_id": user_id,
        "risk_score": round(risk, 2),
        "signals": signals,
        "interpretation": interpret(risk)
    }


def interpret(risk):
    if risk < 20:
        return "Normal autonomy"
    elif risk < 40:
        return "Mild anomaly"
    elif risk < 60:
        return "Elevated pressure"
    elif risk < 80:
        return "High coercion likelihood"
    else:
        return "Critical agency anomaly"