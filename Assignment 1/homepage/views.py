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

# Beautiful Soup
from bs4 import BeautifulSoup
import requests

# Dataframe
import pandas as pd

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
    malaysia_url = 'https://www.worldometers.info/world-population/malaysia-population/'
    malaysia_page = requests.get(malaysia_url)
    malaysia_soup = BeautifulSoup(malaysia_page.text, 'lxml')
    malaysia_pop = malaysia_soup.find('table',attrs={'class':'table table-striped table-bordered table-hover table-condensed table-list'})

    # Obtain every title of columns with tag <th>
    headers = []
    for i in malaysia_pop.find_all('th'):
        title = i.text
        headers.append(title)

    # Renamed column 12
    headers[12] = 'Malaysia Global Rank'

    # Create a dataframe
    malaysia_pop_table = pd.DataFrame(columns = headers)

    # Create a for loop to fill malaysia_pop_table
    for j in malaysia_pop.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(malaysia_pop_table)
        malaysia_pop_table.loc[length] = row

    return render(request, "malaysia.html", malaysia_pop_table)



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
