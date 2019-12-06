import requests
from bs4 import BeautifulSoup


def job_search(HTML):
    r = requests.get(HTML)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all(
        "div", {"class": "jobsearch-SerpJobCard"})
    job_dict = {}
    for result in results:
        title = result.find("div", {"class": "title"}).find("a")["title"]
        company = result.find("span", {"class": "company"}).string
        if company is not None:
            pass
        else:
            try:
                company = result.find("span", {"class": "company"}).find(
                    "a", {"class": "turnstileLink"}).string
            except:
                company = 'No Information'
        company = str(company).strip()
        location = result.find(
            "div", {"class": "recJobLoc"})["data-rc-loc"]
        job_id = result["data-jk"]
        job_dict[title] = [
            company, location, f"https://kr.indeed.com/viewjob?jk={job_id}"]
    return job_dict
