from bs4 import BeautifulSoup
import pandas

html = open("first_page.html", "r", encoding="utf-8")

soup = BeautifulSoup(html, "html.parser")


#Finds all blocks where articles are posted
views_row_divs = soup.find_all("div", attrs={"class" : "views-row"})
description_divs = soup.find_all("div", attrs={"class": "field field--name-body field--type-text-with-summary field--label-hidden field__item"})




df = pandas.DataFrame(columns=["Oferta", "Descripción", "URL"])

print(df)


for row_div, desc_div in zip(views_row_divs, description_divs): #Searchs each Tag in the resulting list.
    title = row_div.article.header.h2.a.text
    #print(title) # Extracts the title

    url = row_div.article.attrs["about"]
    #print(url) #Extracts the url of the offer

    description = desc_div.text
    #print(description) #Extracts description of the offer
    
    row = pandas.DataFrame([[title, description, "https://www.csic.es"+url]], columns=df.columns) # Creates a row DF with same columns as initial one.
    df = pandas.concat([df, row], ignore_index=True)


print(df)


