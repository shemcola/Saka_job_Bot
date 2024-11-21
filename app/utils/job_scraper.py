from bs4 import BeautifulSoup
import requests

def scrape_jobs(search_query, location):
    url = f"https://www.examplejobboard.com/search?q={search_query}&l={location}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    for job_card in soup.find_all("div", class_="job-card"):
        title = job_card.find("h2").text
        company = job_card.find("span", class_="company").text
        location = job_card.find("span", class_="location").text
        link = job_card.find("a")["href"]
        jobs.append({"title": title, "company": company, "location": location, "url": link})

    return jobs
 
