# Django
from django.shortcuts import render
from django.http import HttpResponse
import os

# ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager

# Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import requests

# Create your views here.

def world(request):
    url = 'https://www.worldometers.info/world-population/'
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    world_pop_table = soup.find_all('table',attrs={'class':'table table-hover table-condensed'})
    print(world_pop_table)    
    return render(request, "world.html")

def asia(request):
    return render(request, "asia.html")

def malaysia(request):
    return render(request, "malaysia.html")



def scrap(request):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.worldometers.info/world-population/world-population-by-year/')

    world_table = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/table")

    data_table = {
        'world_table' : world_table.get_attribute('content')
    }

    print(data_table)
    driver.quit()
