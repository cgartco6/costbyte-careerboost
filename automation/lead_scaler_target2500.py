class LeadScaler2500:
    def projected_growth(self, day):
        # simple growth simulation
        return min(2500, int((day ** 2.3) * 7))

    def strategy(self):
        return [
            "Push daily TikTok shorts",
            "Boost Instagram reels",
            "Facebook job groups posting",
            "WhatsApp broadcast lists",
            "High-frequency AI-generated marketing content"
        ]
