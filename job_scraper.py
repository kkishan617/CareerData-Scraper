# Import requests library to send HTTP requests to websites
import requests

# Import BeautifulSoup for parsing and extracting data from HTML
from bs4 import BeautifulSoup

# Import pandas for creating and handling datasets
import pandas as pd


# URL of the website to scrape
url = "https://realpython.github.io/fake-jobs/"

# Send a GET request to the website and store the response
response = requests.get(url)

# Print the HTTP status code (200 means success)
print("Status Code:", response.status_code)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, "html.parser")

# Print the title of the webpage
print("Website Title:", soup.title.text)


# Find all job cards on the webpage
job_cards = soup.find_all("div", class_="card-content")

# Print the total number of job listings found
print("Total Jobs:", len(job_cards))


# Select the first job card for testing
first_job = job_cards[0]

# Extract the job title from the h2 tag
job_title = first_job.find("h2").text.strip()

# Extract the company name from the h3 tag
company = first_job.find("h3").text.strip()

# Extract the location from the p tag
location = first_job.find("p").text.strip()

# Display the extracted details of the first job
print("\nFirst Job Details:")
print("Job Title:", job_title)
print("Company:", company)
print("Location:", location)


# Create an empty list to store all job data
jobs_data = []

# Loop through each job card
for job in job_cards:

    # Extract job title
    title = job.find("h2").text.strip()

    # Extract company name
    company = job.find("h3").text.strip()

    # Extract location
    location = job.find("p").text.strip()

    # Add extracted data to the list
    jobs_data.append([title, company, location])


# Display the first 5 records from the extracted data
print("\nFirst 5 Extracted Records:")
print(jobs_data[:5])


# Convert the extracted data into a Pandas DataFrame
df = pd.DataFrame(
    jobs_data,
    columns=["Job Title", "Company", "Location"]
)

# Display the first 5 rows of the dataset
print("\nDataset Preview:")
print(df.head())


# Save the dataset as a CSV file
df.to_csv("jobs.csv", index=False)

# Print success message
print("\nCSV file created successfully!")