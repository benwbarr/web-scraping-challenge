from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {"executable_path": "/Users/downr/Downloads/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

def scrape():
    final = {}
    output = marsNews()
    final["mars_news"] = output[0]
    final["mars_paragraph"] = output[1]
    final["mars_image"] = marsImage()
    final["mars_weather"] = marsWeather()
    final["mars_facts"] = marsFacts()
    final["mars_hemisphere"] = marsHem()

    return final

def mars_news():
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    text = soup.find("div", class_='list_text')
    news_title = article.find("div", class_="content_title").text
    news_p = article.find("div", class_ ="article_teaser_body").text
    output = [news_title, news_p]
    return output

def mars_image():
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    featured_image_url = "https://www.jpl.nasa.gov" + soup.find("img", class_="thumb")["src"]
    return featured_image_url

def Facts():
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    Mars_facts = pd.read_html(facts_url)
    Facts_df = Mars_facts[0]
    Facts_df.columns = ["Item","Value"]
    return Facts_df

def mHem():
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    hemispheres = []
    items = soup.find("div", class_ = "result-list" )
    hemispheres_mars = products.find_all("div", class_="item")

    for hemisphere in hemispheres_mars:
        title = hemisphere.find("h3").text
        end = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end    
        html = browser.html
        soup=BeautifulSoup(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        hemispheres_mars.append({"title": title, "img_url": image_url})
    return hemispheres_mars    