class ApplicantFollowUpAutomation:
    def build_message(self, email, resume_status):
        if resume_status == "ready":
            return f"Hello {email}, your AI-enhanced resume is ready for download!"
        return f"Hello {email}, we are still processing your resume."

    def send_followup(self, email, status):
        return f"Follow-up sent to {email}: {status}"
