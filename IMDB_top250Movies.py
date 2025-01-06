from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

driver = webdriver.Chrome()

driver.get(url)

movies = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")

movie_list = []

for movie in movies:
    title = movie.find_element(By.CSS_SELECTOR, "h3.ipc-title__text").text.split(".")[1].strip()
    year = movie.find_element(By.CSS_SELECTOR, "span.cli-title-metadata-item").text
    rating = movie.find_element(By.CSS_SELECTOR, "span.ipc-rating-star--rating").text
    movie_list.append({
        "movie_title" : title,
        "released_date" : year,
        "rating" : rating
    })

df = pd.DataFrame(movie_list)

df.to_csv("Top 250 Movies.csv") # Save movie data into a  CSV file
df.to_pickle("Top 250 Movies.pkl") # Save movie data into a pickle file
