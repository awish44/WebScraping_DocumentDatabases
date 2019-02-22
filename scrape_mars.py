import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import numpy as np
import pandas as pd
import regex as re
import requests


def scrape():
    chromedriver = "chromedriver.exe" 
    chromedriver = os.path.expanduser(chromedriver)
    sys.path.append(chromedriver)
    driver = webdriver.Chrome(chromedriver)

    mars_info = {}

    # NASA  Mars news scrape 
    news_url = "https://mars.nasa.gov/news/?page="
    driver.get(news_url)
    time.sleep(1)

    # Scrape recent headlines
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    mars_info['news_title'] = soup.find('div', class_='content_title').text 
    mars_info['news_p'] = soup.find('div', class_='rollover_description_inner').text 

 
    # Scrape featured image from JPL website
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    driver.get(jpl_url)
    time.sleep(1)  
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    img = soup.find('a', class_='fancybox')['data-fancybox-href']

    mars_info['feat_image_url'] = f'https://www.jpl.nasa.gov{img}'
    

    # Scrape twitter weather report 
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    driver.get(weather_url)
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    tweets = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').contents
    tweet_weather = tweets[0]

    mars_info['mars_weather'] = tweet_weather
   


    # Mars Facts
    facts_url = 'https://space-facts.com/mars/'
    facts_tables = pd.read_html(facts_url) 
    facts_df = facts_tables[0]
    facts_df.columns = ['Description', 'Value']
    facts_df = facts_df.set_index('Description')

    mars_info['mars_facts'] = facts_df.to_html()



    # Mars Hemispheres
    hemisphere_url = 'https://astrogeology.usgs.gov/maps/mars-viking-hemisphere-point-perspectives'
    response = requests.get(hemisphere_url)
    soup = BeautifulSoup(response.text, "html.parser")
    heading = soup.find_all('h3') 
    heading_data = heading

    # Clean the headings up and only extract the text 
    # Make a dictionary in order to pair the image URL for final results
    head = [x.text.split('>')[-1].strip() for x in heading_data]

    titles = []

    for x in head:
        title = x
        titles.append(title)

    # Extract only the titles that have "Enhanced" 
    enhanced_title = [s for s in titles if "Enhanced" in s]

    # Get the links for each image
    hemis = soup.find_all('a', {'class': 'item', 'href': True})
    hemi_img_links = []

    for hemi in hemis:
        link = (hemi['href'])
        hemi_link = 'https://astrogeology.usgs.gov'+ link
        hemi_img_links.append(hemi_link)

    # Extract only the links that have "Enhanced"
    enhanced_link = [s for s in hemi_img_links if "_enhanced" in s]

    # Get the links for each image
    list_links = []

    for hemi in enhanced_link:
        response = requests.get(hemi)
        soup = BeautifulSoup(response.text, "html.parser")
        lists = soup.find_all('ul')[6]
        for litag in lists.find_all('li'):
            for link in litag.find_all('a', href=True):
                links = link['href']
                list_links.append(links)

    # Extract only the links that have ".jpg"
    jpg_links = [s for s in list_links if ".jpg" in s]

    hemisphere_image_urls = [{'title': enhanced_title[0], 'img_url': jpg_links[0]}, 
                        {'title': enhanced_title[1], 'img_url': jpg_links[1]},
                        {'title': enhanced_title[2], 'img_url': jpg_links[2]},
                        {'title': enhanced_title[3], 'img_url': jpg_links[3]}]

    mars_info['mars_hemispheres'] = hemisphere_image_urls

    return mars_info    