import datetime
import statistics
from collections import defaultdict

# Create a living baseline of every user

class BaselineEngine:
    def __init__(self):
        self.user_profiles = defaultdict(dict)

    def update_user_profiles(self, user_id, events):
        amounts = [e['amount'] for e in events]
        times = [
            datetime.fromisoformat(e["timestamp"]).timestamp()
            for e in events
        ]
        recipients = [e["recipient"] for e in events]
        nav_times = [e["navigation_time_ms"] for e in events]

        profile = {
            "mean_amount": statistics.mean(amounts),
            "std_amount": statistics.stdev(amounts) if len(amounts) > 1 else 0,
            "mean_time": statistics.mean(times),
            "std_time": statistics.stdev(times) if len(times) > 1 else 1,
            "top_recipients": list(set(recipients)) if recipients else [],
            "mean_nav_time": statistics.mean(nav_times),
            "std_nav_time": statistics.stdev(nav_times) if len(nav_times) > 1 else 1,
            "updated_at": datetime.datetime.now().isoformat()
        }

        self.user_profiles[user_id] = profile
        return profile