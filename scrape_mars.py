from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {"executable_path": "/Users/downr/Downloads/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

def scrape():
