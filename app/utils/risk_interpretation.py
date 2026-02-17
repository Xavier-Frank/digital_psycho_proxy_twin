
class RiskInterpretation:
    def classify_psychological_intent(self, risk_score):
        if risk_score < 30:
            return "LOW"
        elif risk_score < 55:
            return "NORMAL"
        elif risk_score < 75:
            return "POSSIBLE_COERCION"
        else:
            return "HIGH_RISK_COERCION"