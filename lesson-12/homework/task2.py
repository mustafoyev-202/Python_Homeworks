import requests
from bs4 import BeautifulSoup
import sqlite3
import csv


# Function to scrape job listings
def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for job_element in soup.find_all("div", class_="card-content"):
        job_title = job_element.find("h2", class_="title").text.strip()
        company_name = job_element.find("h3", class_="company").text.strip()
        location = job_element.find("p", class_="location").text.strip()
        application_link = job_element.find_all("a", class_="card-footer-item")[1][
            "href"
        ].strip()

        # Fetch job description from the application link
        job_response = requests.get(application_link)
        job_soup = BeautifulSoup(job_response.text, "html.parser")
        job_description_tag = job_soup.find("div", class_="content").find("p")
        job_description = (
            job_description_tag.text.strip()
            if job_description_tag
            else "No description available"
        )

        jobs.append(
            (job_title, company_name, location, job_description, application_link)
        )

    return jobs


# Function to store job listings into SQLite database
def store_jobs(jobs):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS jobs (
            job_title TEXT,
            company_name TEXT,
            location TEXT,
            job_description TEXT,
            application_link TEXT,
            PRIMARY KEY (job_title, company_name, location)
        )
    """
    )

    for job in jobs:
        cursor.execute(
            """
            INSERT OR IGNORE INTO jobs (job_title, company_name, location, job_description, application_link)
            VALUES (?, ?, ?, ?, ?)
        """,
            job,
        )

        cursor.execute(
            """
            UPDATE jobs
            SET job_description = ?, application_link = ?
            WHERE job_title = ? AND company_name = ? AND location = ?
        """,
            (job[3], job[4], job[0], job[1], job[2]),
        )

    conn.commit()
    conn.close()


# Function to filter job listings by location or company name
def filter_jobs(location=None, company_name=None):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location = ?"
        params.append(location)
    if company_name:
        query += " AND company_name = ?"
        params.append(company_name)

    cursor.execute(query, params)
    filtered_jobs = cursor.fetchall()
    conn.close()
    return filtered_jobs


# Function to export filtered results into a CSV file
def export_to_csv(filtered_jobs, filename="filtered_jobs.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "Job Title",
                "Company Name",
                "Location",
                "Job Description",
                "Application Link",
            ]
        )
        writer.writerows(filtered_jobs)


# Main execution
if __name__ == "__main__":
    jobs = scrape_jobs()
    store_jobs(jobs)
    filtered_jobs = filter_jobs(location="Remote")
    export_to_csv(filtered_jobs)
