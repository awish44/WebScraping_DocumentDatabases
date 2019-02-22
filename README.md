# WebScraping_DocumentDatabases
Web application built with Flask, Python, ChromeDriver, BeautifulSoup, PyMongo & Bootstrap that scrapes various websites for data related to the Mission to Mars and rendered on an HTML page.

## Sites Scraped:

* **NASA Mars News: ** [NASA Mars News Site](https://mars.nasa.gov/news/) to collect the latest News Title and Paragraph Text.

* **JPL Mars Space Images - Featured Image:** Navigate the [site](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) and find the image url for the current Featured Mars 

* **Mars Weather:** Mars Weather [twitter account](https://twitter.com/marswxreport?lang=en) to scrape the latest Mars weather tweet.

* **Mars Facts:** Visit the Mars Facts [webpage](http://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet then convert the data to a HTML table string.

* **Mars Hemispheres:** Used the [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

## MongoDB and Flask Application

* Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Converted Jupyter notebook into a Python script called with a function called `scrape` that executes all of the scraping code from above and returned one Python dictionary containing all of the scraped data.

* Created a route called `/scrape` that imported the python script and called my `scrape` function.

 * Stored the return value in Mongo as a Python dictionary.

* Created a root route `/` to query Mongo database and pass the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that took the mars data dictionary and displayed all of the data in the appropriate HTML elements. 
