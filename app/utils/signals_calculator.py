# Time deviation
from datetime import datetime


def calculate_time_deviation(session: dict, baseline: dict):
    session_time = datetime.fromisoformat(session["timestamp"]).hour
    mean_time = baseline["mean_time"]
    std_time = baseline["std_time"] if baseline["std_time"] != 0 else 1  # avoid division by zero

    return abs(session_time - mean_time) / std_time

    # Amount deviation
def calculate_amount_deviation(session: dict, baseline : dict):
    std_amount = baseline["std_amount"] if baseline["std_amount"] != 0 else 1
    return abs(session["amount"] - baseline["mean_amount"]) / std_amount

    # Recipient familiarity

def calculate_recipient_familiarity(session: dict, baseline : dict):
    return 1 if session["recipient"] in baseline["top_recipients"] else 0

    # Navigation speed deviation
def calculate_speed_deviation(session: dict, baseline : dict):
    std_nav_time = baseline["std_nav_time"] if baseline["std_nav_time"] != 0 else 1
    return abs(session["navigation_time_ms"] - baseline["mean_nav_time"]) / std_nav_time