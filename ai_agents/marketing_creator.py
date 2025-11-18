import random
from datetime import datetime

class MarketingCreator:
    def __init__(self):
        self.topics = [
            "CareerBoost Success Story!",
            "CV Rewrite Transformations",
            "Job Search Power Tips",
            "AI-driven Career Automation"
        ]

    def generate_caption(self):
        t = random.choice(self.topics)
        return f"{t} – Powered by CostByte CareerBoost – {datetime.utcnow()}"

    def create_ad_script(self):
        return """
        🎯 COSTBYTE CareerBoost
        Upload your CV → We rewrite → We apply → You get hired.
        Full automation. AI-powered. Professional. South Africa only.
        """

    def generate_voiceover(self):
        return "AI generated voiceover: 'Welcome to CareerBoost, your path to smarter job success!'"
