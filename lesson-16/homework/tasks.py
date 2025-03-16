import sqlite3
import pandas as pd

# Part 1: Reading Files

# chinook.db
conn = sqlite3.connect("chinook.db")
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print(customers_df.head(10))

# iris.json
iris_df = pd.read_json("iris.json")
print(iris_df.shape)
print(iris_df.columns)

# titanic.xlsx
titanic_df = pd.read_excel("titanic.xlsx")
print(titanic_df.head())

# Flights parquet file
flights_df = pd.read_parquet("flights.parquet")
print(flights_df.info())

# movie.csv
movie_df = pd.read_csv("movie.csv")
print(movie_df.sample(10))

# Part 2: Exploring DataFrames

# Using the DataFrame from iris.json
iris_df.columns = iris_df.columns.str.lower()
iris_selected_df = iris_df[["sepal_length", "sepal_width"]]
print(iris_selected_df.head())

# From the titanic.xlsx DataFrame
titanic_filtered_df = titanic_df[titanic_df["age"] > 30]
print(titanic_filtered_df.head())
print(titanic_df["sex"].value_counts())

# From the Flights parquet file
flights_selected_df = flights_df[["origin", "dest", "carrier"]]
print(flights_selected_df.head())
print(flights_df["dest"].nunique())

# From the movie.csv file
movie_filtered_df = movie_df[movie_df["duration"] > 120]
movie_sorted_df = movie_filtered_df.sort_values(
    by="director_facebook_likes", ascending=False
)
print(movie_sorted_df.head())

# Part 3: Challenges and Explorations

# From iris.json
print(iris_df.describe().loc[["mean", "50%", "std"]])

# From titanic.xlsx
print(titanic_df["age"].agg(["min", "max", "sum"]))

# From movie.csv
director_likes = movie_df.groupby("director_name")["director_facebook_likes"].sum()
print(director_likes.idxmax())
print(movie_df.nlargest(5, "duration")[["title", "director_name"]])

# From Flights parquet file
print(flights_df.isnull().sum())
flights_df.fillna(flights_df.mean(), inplace=True)
print(flights_df.head())
