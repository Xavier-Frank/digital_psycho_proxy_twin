def deviation(current, baseline):
    if baseline == 0:
        return 0
    return abs(current - baseline) / baseline


def psych_risk(signals, baseline):
    weights = {
        "step_delay": 0.15,
        "session_time": 0.15,
        "corrections": 0.15,
        "retries": 0.10,
        "backtracks": 0.15,
        "pin_delay": 0.15,
        "amount_hesitation": 0.15
    }

    score = 0

    for key, w in weights.items():
        score += w * deviation(signals[key], baseline[f"avg_{key}"])

    # normalize to 0–100
    risk = min(score * 100, 100)

    # coercion signature boost
    if (
            signals["linear_flow"] and
            signals["corrections"] == 0 and
            signals["retries"] == 0 and
            signals["backtracks"] == 0 and
            signals["step_delay"] < 0.5
    ):
        risk += 20

    return min(risk, 100)