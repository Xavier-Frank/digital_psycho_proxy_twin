
class RiskEngine:
    WEIGHTS = {
        "time_deviation": 0.25,
        "amount_deviation": 0.30,
        "recipient_familiarity": 0.25,
        "speed_deviation": 0.25
    }

    def compute_risk(self, signals):
        risk = 0

        for k, w in self.WEIGHTS.items():
            value = signals[k]

            if k == "recipient_familiarity":
                value = 1 - value  #sending money to unknown person is risky

            risk += w * value

            return round(risk * 100, 2)
