import requests

def auto_apply(job, user_resume_pdf, user_email):
    data = {
        "job_title": job["title"],
        "cv_url": user_resume_pdf,
        "email": user_email
    }
    # fake send to employer
    print("Applied →", data)
    return True
