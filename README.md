# WebScraping_DocumentDatabases
Web application built with Flask, Python, ChromeDriver, BeautifulSoup, PyMongo & Bootstrap that scrapes various websites for data related to the Mission to Mars and rendered on an HTML page.

**View my final codes here:**
* [Jupyter Notebook Code](mission_to_mars.ipynb)
* [Python Scrape Function](scrape_mars.py)
* [Flask App](app.py)
* [HTML Page](templates/index.html)

## Sites Scraped:

* **NASA Mars News:** Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) to collect the latest News Title and Paragraph Text.

* **JPL Mars Space Images - Featured Image:** Navigate the [site](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) and find the image url for the current Featured Mars 

* **Mars Weather:** Mars Weather [twitter account](https://twitter.com/marswxreport?lang=en) to scrape the latest Mars weather tweet.

* **Mars Facts:** Visit the Mars Facts [webpage](http://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet then convert the data to a HTML table string.

* **Mars Hemispheres:** Used the [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

## MongoDB and Flask Application

* Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Converted Jupyter notebook into a Python script called with a function called `scrape` that executes all of the scraping code.

* Created a routes to leverage Mongo Database and `/scrape` function.

* Created a template HTML file called `index.html` that displayed all of the data in the appropriate HTML elements. 

# My Final Site:

![finalapp_p1.PNG](images/finalapp_p1.PNG)
![finalapp_p2.PNG](images/finalapp_p2.PNG)

