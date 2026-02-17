import os

class Configs:
    # Learning thresholds
    MIN_SESSIONS = int(os.getenv("MIN_SESSIONS", 2))
