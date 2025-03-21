import pandas as pd
import sqlite3

# Merging and Joining
# Inner Join on Chinook Database
conn = sqlite3.connect("chinook.db")
customers = pd.read_sql_query("SELECT * FROM customers", conn)
invoices = pd.read_sql_query("SELECT * FROM invoices", conn)
inner_join = pd.merge(customers, invoices, on="CustomerId")
total_invoices_per_customer = inner_join.groupby("CustomerId").size()

# Outer Join on Movie Data
movies = pd.read_csv("movie.csv")
df1 = movies[["director_name", "color"]]
df2 = movies[["director_name", "num_critic_for_reviews"]]
left_join = pd.merge(df1, df2, on="director_name", how="left")
full_outer_join = pd.merge(df1, df2, on="director_name", how="outer")
left_join_rows = len(left_join)
full_outer_join_rows = len(full_outer_join)

# Grouping and Aggregating
# Grouped Aggregations on Titanic
titanic = pd.read_csv("titanic.csv")
grouped_titanic = (
    titanic.groupby("Pclass")
    .agg({"Age": "mean", "Fare": "sum", "PassengerId": "count"})
    .rename(columns={"PassengerId": "Passenger_Count"})
)

# Multi-level Grouping on Movie Data
grouped_movies = movies.groupby(["color", "director_name"]).agg(
    {"num_critic_for_reviews": "sum", "duration": "mean"}
)

# Nested Grouping on Flights
flights = pd.read_csv("flights.csv")
grouped_flights = (
    flights.groupby(["Year", "Month"])
    .agg({"FlightNum": "count", "ArrDelay": "mean", "DepDelay": "max"})
    .rename(columns={"FlightNum": "Total_Flights"})
)


# Applying Functions
# Apply a Custom Function on Titanic
def classify_age(age):
    return "Child" if age < 18 else "Adult"


titanic["Age_Group"] = titanic["Age"].apply(classify_age)

# Normalize Employee Salaries
employees = pd.read_csv("employee.csv")
employees["Normalized_Salary"] = employees.groupby("Department")["Salary"].transform(
    lambda x: (x - x.mean()) / x.std()
)


# Custom Function on Movies
def classify_duration(duration):
    if duration < 60:
        return "Short"
    elif 60 <= duration <= 120:
        return "Medium"
    else:
        return "Long"


movies["Duration_Class"] = movies["duration"].apply(classify_duration)

# Using pipe
# Pipeline on Titanic
def filter_survived(df):
    return df[df["Survived"] == 1]


def fill_missing_age(df):
    df["Age"].fillna(df["Age"].mean(), inplace=True)
    return df


def create_fare_per_age(df):
    df["Fare_Per_Age"] = df["Fare"] / df["Age"]
    return df


titanic_pipeline = (
    titanic.pipe(filter_survived).pipe(fill_missing_age).pipe(create_fare_per_age)
)


# Pipeline on Flights
def filter_delayed_flights(df):
    return df[df["DepDelay"] > 30]


def add_delay_per_hour(df):
    df["Delay_Per_Hour"] = df["DepDelay"] / df["AirTime"]
    return df


flights_pipeline = flights.pipe(filter_delayed_flights).pipe(add_delay_per_hour)
