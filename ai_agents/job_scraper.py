import requests
from bs4 import BeautifulSoup

def scrape_jobs(keyword="developer", location="South Africa"):
    url = f"https://www.careerjet.co.za/search/jobs?s={keyword}&l={location}"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    jobs = []

    for job in soup.select(".job"):
        jobs.append({
            "title": job.select_one(".title").get_text(strip=True),
            "company": job.select_one(".company").get_text(strip=True),
            "link": job.select_one("a")["href"]
        })

    return jobs
