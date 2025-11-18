import random
from datetime import datetime

class JobScraper:
    def scrape(self, keyword="general work"):
        return [
            {
                "title": f"{keyword.title()} Position #{i}",
                "company": "Company " + chr(65+i),
                "location": random.choice(["Johannesburg", "Cape Town", "Remote", "Pretoria"]),
                "url": f"https://jobs.example.com/{keyword}/{i}",
                "scraped_at": datetime.utcnow()
            }
            for i in range(1, 6)
        ]
