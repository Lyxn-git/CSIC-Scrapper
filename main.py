import requests
from bs4 import BeautifulSoup
import pandas as pd



base_url = "https://www.csic.es/es/modalidad-predoctoral-bdei/ayudas-para-contratos-predoctorales-para-la-formacion-de-doctores?page="
page_number = 0


df = pd.DataFrame(columns=["Oferta", "Descripción", "URL"])

while True: #Iterate over all pages
    response = requests.get(url=base_url+str(page_number)) #gets the html of webpage using page number and base url
    soup = BeautifulSoup(response.text, "html.parser") #parses it as Soup Object
    
    
    article = soup.find("article")
    if article == None: #Checks if page is empty
        break

    if page_number > 30: #failsafe method to not iterate to infinity
        break


    views_row_divs = soup.find_all("div", attrs={"class" : "views-row"}) # finds all divs which class is "views-row"
    description_divs = soup.find_all("div", attrs={"class": "field field--name-body field--type-text-with-summary field--label-hidden field__item"}) # finds all divs which class is "field field..."

    page_df = pd.DataFrame(columns=df.columns)

    for row_div, desc_div in zip(views_row_divs, description_divs):
        title = row_div.article.header.h2.a.text # Extracts the title of the header
        description = desc_div.text # Extracts description of the offer
        url = row_div.article.attrs["about"] # Extracts relative url of the offer

        complete_url = "https://www.csic.es" + url
        row = [title, description, complete_url]

        row_df = pd.DataFrame([row], columns=df.columns)

        df = pd.concat([df, row_df], ignore_index=True)

 
    page_number += 1 #Goes to next page

df.to_excel("output.xlsx")
print(df)