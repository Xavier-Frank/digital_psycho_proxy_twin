def extract_signals(session):
    return {
        "step_delay": session["step_delay"],
        "session_time": session["session_time"],
        "corrections": session["corrections"],
        "retries": session["retries"],
        "backtracks": session["backtracks"],
        "pin_delay": session["pin_delay"],
        "amount_hesitation": session["amount_hesitation"],
        "linear_flow": session["linear_flow"]
    }
