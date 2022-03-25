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

# Visualization
import matplotlib.pyplot as plt

#####################################################################################################################################

def world(request):
    world_url = 'https://www.worldometers.info/world-population/'
    world_page = requests.get(world_url)
    world_soup = BeautifulSoup(world_page.text, 'lxml')
    world_pop = world_soup.find('table',attrs={'class':'table table-striped table-bordered table-hover table-condensed table-list'})

    # Obtain every title of columns with tag <th>
    headers = []
    for i in world_pop.find_all('th'):
        title = i.text
        headers.append(title)

    # Renamed column 0
    headers[0] = "Year"

    # Create a dataframe
    world_pop_table = pd.DataFrame(columns = headers)

    # Create a for loop to fill world_pop_table
    for j in world_pop.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(world_pop_table)
        world_pop_table.loc[length] = row

    context = { "world": world_pop_table.to_html() }

    print(world_pop_table.to_html())

    return render(request, "world.html", context) 


#####################################################################################################################################

def asia(request):
    asia_url = 'https://www.worldometers.info/world-population/asia-population/'
    asia_page = requests.get(asia_url)
    asia_soup = BeautifulSoup(asia_page.text, 'lxml')
    asia_pop = asia_soup.find('table',attrs={'class':'table table-striped table-bordered table-hover table-condensed table-list'})

    # Obtain every title of columns with tag <th>
    headers = []
    for i in asia_pop.find_all('th'):
        title = i.text
        headers.append(title)

    # Renamed column 10
    headers[10] = "Asia's Share of World Pop"

    # Create a dataframe
    asia_pop_table = pd.DataFrame(columns = headers)

    # Create a for loop to fill malaysia_pop_table
    for j in asia_pop.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(asia_pop_table)
        asia_pop_table.loc[length] = row
    
    context = { "asia": asia_pop_table.to_html() }

    print(asia_pop_table.to_html())

    return render(request, "asia.html", context)


#####################################################################################################################################

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
    #context = dict(malaysia_pop_table.values)
    context = { "data": malaysia_pop_table.to_html() }

    #print(context)
    print(malaysia_pop_table.to_html())

    return render(request, "malaysia.html", context)
    # HttpResponse(malaysia_pop_table.to_html())

def malaysia_bar(request):
    malaysia_url = 'https://www.worldometers.info/world-population/malaysia-population/'
    malaysia_page = requests.get(malaysia_url)
    malaysia_soup = BeautifulSoup(malaysia_page.text, 'lxml')
    malaysia_city_pop = malaysia_soup.find('table',attrs={'class':'table table-hover table-condensed table-list'})

    # Obtain every title of columns with tag <th>
    headers_city = []
    for i in malaysia_city_pop.find_all('th'):
        title = i.text
        headers_city.append(title)

    # Create a dataframe
    malaysia_city_pop_table = pd.DataFrame(columns = headers_city)

    # Create a for loop to fill malaysia_pop_table
    for j in malaysia_city_pop.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(malaysia_city_pop_table)
        malaysia_city_pop_table.loc[length] = row
    
    #drop 1st column
    malaysia_city_pop_table = malaysia_city_pop_table.iloc[: , 1:]

    # creating the dataset
    city = malaysia_city_pop_table['CITY NAME'].head(12)
    population = malaysia_city_pop_table['POPULATION'].head(12)
    
    # Figure Size
    fig = plt.figure(figsize =(20, 7))
    
    # Horizontal Bar Plot
    # plt.bar(city[0:10], population[0:10])
    plt.bar(city, population, color ='maroon', width = 0.8)

    plt.xlabel("City Name")
    plt.ylabel("Population")
    plt.title("Main Cities by Population in Malaysia")
    
    # Show Plot
    plot_chart = plt.show()

    context_chart = { "chart": plot_chart.to_html() }
    
    print(plot_chart.to_html())

    return render(request, "malaysia.html", context_chart)



# def scrap(request):
#     options = Options()
#     options.headless = True
#     options.add_argument("--window-size=1920,1080")

#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.get('https://www.worldometers.info/world-population/world-population-by-year/')

#     world_table = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/table")

#     data_table = {
#         'world_table' : world_table.get_attribute('content')
#     }

#     print(data_table)
#     driver.quit()
