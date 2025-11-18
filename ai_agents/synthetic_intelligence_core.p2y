import re
import uuid
from datetime import datetime

class SyntheticIntelligenceCore:
    def __init__(self):
        self.model = "Synthetic-Intelligence-Core-v1"
        self.version = "1.0.0"

    def clean_text(self, text: str) -> str:
        text = re.sub(r"\s+", " ", text)
        text = text.replace("•", "-")
        return text.strip()

    def rewrite_resume(self, raw_text: str, name: str, skills: list, qualifications: list):
        cleaned = self.clean_text(raw_text)

        rewritten = f"""
        PROFESSIONAL RESUME – AUTO-GENERATED
        ID: {uuid.uuid4()}

        NAME: {name.upper()}
        DATE GENERATED: {datetime.utcnow()}

        SUMMARY:
        A highly motivated professional with a strong skillset and experience. AI-enhanced rewrite improves clarity, structure and professional tone.

        KEY SKILLS:
        {chr(10).join(['- ' + s for s in skills])}

        QUALIFICATIONS:
        {chr(10).join(['- ' + q for q in qualifications])}

        EXPERIENCE (AI RESTRUCTURED):
        {cleaned}

        END OF DOCUMENT
        """

        return rewritten.strip()
