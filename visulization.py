import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("jobs.csv")

job_titles = df["Job Title"].value_counts().head(10)

job_titles.plot(kind="bar")

plt.title("Top 10 Job Titles")
plt.xlabel("Job Title")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("top_job_titles.png")

plt.show()

companies = df["Company"].value_counts().head(10)

companies.plot(kind="bar")

plt.title("Top Hiring Companies")
plt.xlabel("Company")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("top_companies.png")

plt.show()

locations = df["Location"].value_counts().head(10)

locations.plot(kind="bar")

plt.title("Top Job Locations")
plt.xlabel("Location")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("top_locations.png")

plt.show()

df["Company"].value_counts().head(5).plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Top Hiring Companies Distribution")

plt.ylabel("")

plt.savefig("company_pie_chart.png")

plt.show()

df["Location"].value_counts().head(5).plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Location Distribution")

plt.ylabel("")

plt.savefig("location_pie_chart.png")

plt.show()


