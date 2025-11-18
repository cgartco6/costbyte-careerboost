import os
from ai_resume_writer import write_resume

async def process_resume(user_id, resume_file, photo_file, qual_file):
    base = f"data/{user_id}"
    os.makedirs(base, exist_ok=True)

    resume_path = f"{base}/resume_raw.pdf"
    photo_path = f"{base}/photo.jpg"
    qual_path = f"{base}/qualifications.pdf"
    final_resume_path = f"{base}/final_resume.pdf"

    with open(resume_path, "wb") as f:
        f.write(await resume_file.read())
    with open(photo_path, "wb") as f:
        f.write(await photo_file.read())
    with open(qual_path, "wb") as f:
        f.write(await qual_file.read())

    write_resume(
        name="Applicant",
        experience=["Extracted experience from AI..."],
        skills=["AI Extracted Skills"],
        qualifications=["AI Extracted Qualifications"],
        photo_path=photo_path,
        output_path=final_resume_path
    )

    return {
        "resume": resume_path,
        "photo": photo_path,
        "qualifications": qual_path,
        "final_resume": final_resume_path
    }
