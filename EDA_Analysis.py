
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("jobs.csv")

print(df.head())

print(df.info())

print(df.describe(include="all"))

# Check for missing values
print(df.isnull().sum())

# Check for duplicate records
print(df.duplicated().sum())

# Display top 10 most common job titles
print(df["Job Title"].value_counts().head(10))

# Display top 10 hiring companies
print(df["Company"].value_counts().head(10))

# Display top 10 job locations
print(df["Location"].value_counts().head(10))

# -----------------------------------------
# Top Job Titles Visualization
# -----------------------------------------
df["Job Title"].value_counts().head(10).plot(kind="bar")

plt.title("Top Job Titles")
plt.tight_layout()

plt.savefig("top_job_titles.png")
plt.show()

# -----------------------------------------
# Top Hiring Companies Visualization
# -----------------------------------------
df["Company"].value_counts().head(10).plot(kind="bar")

plt.title("Top Hiring Companies")
plt.tight_layout()

plt.savefig("top_companies.png")
plt.show()

# -----------------------------------------
# Top Job Locations Visualization
# -----------------------------------------
df["Location"].value_counts().head(10).plot(kind="bar")

plt.title("Top Job Locations")
plt.tight_layout()

plt.savefig("top_locations.png")
plt.show()