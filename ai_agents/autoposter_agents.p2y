class AutoPosterAgents:
    def __init__(self):
        self.status = []

    def apply_for_job(self, job, user_profile):
        report = {
            "job_title": job["title"],
            "status": "APPLIED",
            "user": user_profile.get("email"),
            "submitted_to": job["url"]
        }
        self.status.append(report)
        return report

    def apply_bulk(self, jobs, user_profile):
        return [self.apply_for_job(j, user_profile) for j in jobs]
