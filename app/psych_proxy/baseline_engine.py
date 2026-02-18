from datetime import datetime
import statistics
from collections import defaultdict

# Create a living baseline of every user

class BaselineEngine:
    def __init__(self):
        self.user_profiles = defaultdict(dict)

    def update_user_profiles(self, user_id, events):
        amounts = [e['amount'] for e in events]
        hours = [
            datetime.fromisoformat(e["timestamp"]).hour
            for e in events
        ]
        recipients = [e["recipient"] for e in events]
        nav_times = [e["navigation_time_ms"] for e in events]

        profile = {
            "mean_amount": statistics.mean(amounts),
            "std_amount": statistics.stdev(amounts) if len(amounts) > 1 else 0,
            "mean_time": statistics.mean(hours),
            "std_time": statistics.stdev(hours) if len(events) > 1 else 0,
            "top_recipients": list(set(recipients)) if recipients else [],
            "mean_nav_time": statistics.mean(nav_times),
            "std_nav_time": statistics.stdev(nav_times) if len(nav_times) > 1 else 1,
            "updated_at": datetime.now().isoformat()
        }

        self.user_profiles[user_id] = profile
        return profile