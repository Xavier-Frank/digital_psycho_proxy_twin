# Time deviation
def calculate_time_deviation(session: dict, baseline : dict):
    return abs(session["timestamp"].hour - baseline["mean_time"]) / baseline["std_time"]

    # Amount deviation
def calculate_amount_deviation(session: dict, baseline : dict):
    return abs(session["amount"] - baseline["mean_amount"]) / baseline["std_amount"]

    # Recipient familiarity

def calculate_recipient_familiarity(session: dict, baseline : dict):
    return 1 if session["recipient"] in baseline["top_recipients"] else 0

    # Navigation speed deviation
def calculate_speed_deviation(session: dict, baseline : dict):
    return abs(session["navigation_time_ms"] - baseline["mean_nav_time"]) / baseline["std_nav_time"]