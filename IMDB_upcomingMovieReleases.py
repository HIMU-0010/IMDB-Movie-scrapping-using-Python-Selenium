from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

url = "https://www.imdb.com/calendar/?ref_=rlm&region=US&type=MOVIE"

driver = webdriver.Chrome()

driver.get(url)

articles = driver.find_elements(By.CSS_SELECTOR, "article.sc-fb872901-1")

movie_data = []

for article in articles:
    date = article.find_element(By.CSS_SELECTOR, "h3.ipc-title__text").text
    title = article.find_element(By.CSS_SELECTOR, "a.ipc-metadata-list-summary-item__t").text.split("(")[0].strip()
    movie_data.append({
        "movie_title" : title,
        "release_date" : date
    })

df = pd.DataFrame(movie_data)

df.to_csv("Upcoming Movies.csv") # Save movie data into a  CSV file
df.to_pickle("Upcoming Movies.pkl") # Save movie data into a pickle file
