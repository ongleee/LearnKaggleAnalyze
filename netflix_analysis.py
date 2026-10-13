import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix_titles.csv")

print(df.isnull().sum().sort_values(ascending=False))

# ตรวจสอบแถวซ้ำ
print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

# แปลงวันที่เป็น datetime
df["date_added"] = pd.to_datetime(
    df["date_added"].str.strip(),
    errors="coerce"
)

# สร้างคอลัมน์ปีที่เพิ่มเข้า Netflix
df["year_added"] = df["date_added"].dt.year

type_counts = df["type"].value_counts()

print(type_counts)
type_counts.plot(
    kind="bar",
    title="Movies vs TV Shows on Netflix",
    xlabel="Content Type",
    ylabel="Number of Titles",
    rot=0
)

plt.tight_layout()
plt.show()


countries = (
    df["country"]
    .dropna()
    .str.split(", ")
    .explode()
    .str.strip()
)

top_countries = countries.value_counts().head(10)


print(top_countries)

top_countries.sort_values().plot(
    kind="barh",
    title="Top 10 Countries by Content Listings",
    xlabel="Number of Listings",
    ylabel="Country"
)

plt.tight_layout()
plt.show()

added_per_year = df["year_added"].value_counts().sort_index()

print(added_per_year)

added_per_year.plot(
    kind="line",
    marker="o",
    title="Netflix Titles Added by Year",
    xlabel="Year Added",
    ylabel="Number of Titles"
)

plt.tight_layout()
plt.show()


movies = df[df["type"] == "Movie"].copy()

movies["duration_minutes"] = pd.to_numeric(
    movies["duration"].str.extract(r"(\d+)")[0],
    errors="coerce"
)

print(movies["duration_minutes"].describe())

sns.histplot(
    data=movies,
    x="duration_minutes",
    bins=30
)

plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.show()


ratings = df["rating"].value_counts().head(10)

print(ratings)

ratings.sort_values().plot(
    kind="barh",
    title="Top Content Ratings",
    xlabel="Number of Titles",
    ylabel="Rating"
)

plt.tight_layout()
plt.show()
