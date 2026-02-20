
class RiskEngine:
    WEIGHTS = {
        "time_deviation": 0.05,
        "amount_deviation": 0.35,
        "recipient_familiarity": 0.55,
        "speed_deviation": 0.05
    }

    def compute_risk(self, signals):
        risk = 0

        for k, w in self.WEIGHTS.items():
            value = signals[k]

            if k == "recipient_familiarity":
                value = 1 - value  #sending money to unknown person is risky

            risk += w * value

            return round(risk * 100, 2)
