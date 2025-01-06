## IMDb Movie Scraper

**Description:**

-This Python project provides two web scraping scripts using Selenium to extract movie data from IMDb:

1. **Top 250 Movies:**
   -Scrapes the "Top 250 Movies" list on IMDb and saves the information (title, release date, rating) in a CSV and pickle file.
2. **Upcoming Movies:**
    -Scrapes the "Upcoming Releases" section on IMDb and saves the movie titles and release dates in a CSV and pickle file.

**Requirements:**

* Python 3.x
* Selenium library 
* Pandas library 

**Instructions:**

1. **Install Dependencies:** 
   ```bash
   pip install selenium pandas
   
2. **Download ChromeDriver (if necessary):**
   If you're using Chrome for web scraping, you'll need the appropriate ChromeDriver version for your Chrome browser. Download it from the official website (https://developer.chrome.com/docs/chromedriver/downloads) and extract the executable file to a suitable location in your system path.
Run the Scripts:

**To scrape the Top 250 Movies list:**

```bash
python top_250_movies.py
```
To scrape the Upcoming Movies section:

```bash
python upcoming_movies.py
```
**The scraped data will be saved as "Top 250 Movies.csv", "Top 250 Movies.pkl", "Upcoming Movies.csv", and "Upcoming Movies.pkl" in your project directory.**

**Usage:**

These scripts are intended for educational purposes and personal use. Be mindful of IMDb's terms of service and avoid excessive scraping that might overload their servers.

**Additional Notes:**

You can modify the CSS selectors in the code to target specific elements on the IMDb website if the structure changes in the future.
Consider incorporating error handling mechanisms in your code to gracefully handle unexpected situations during scraping.
