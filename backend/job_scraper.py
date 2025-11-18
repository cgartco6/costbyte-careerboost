import requests
from bs4 import BeautifulSoup

def scrape_jobs(keyword="software", location="south africa"):
    url = f"https://www.indeed.com/jobs?q={keyword}&l={location}"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    jobs = []

    for div in soup.select(".result"):
        title = div.select_one(".jobTitle").text.strip()
        company = div.select_one(".companyName").text.strip()
        jobs.append({"title": title, "company": company})

    return jobs
