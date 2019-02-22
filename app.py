from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect
import scrape_mars

# Create instance of Flask
app = Flask(__name__)

# Set up Mongo connection
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route to render index.html template
@app.route("/")
def index():
    mars_info = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_info=mars_info)

# Route that triggers the scrape function
@app.route("/scrape")
def mars_scrape():
    mars_info = mongo.db.mars_info
    mars_data = scrape_mars.scrape()
    mars_info.update({}, mars_data, upsert=True)
    # Redirect back to homepage
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run(debug=True)