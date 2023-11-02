import requests
from bs4 import BeautifulSoup

test_page = "https://www.csic.es/es/modalidad-predoctoral-bdei/ayudas-para-contratos-predoctorales-para-la-formacion-de-doctores?page=0"

response = requests.get(url=test_page)

soup = BeautifulSoup(response.text, "html.parser")

test_file = "first_page.html"

with open(test_file, "w", encoding="utf-8") as file:
    file.write(response.text)
        



print(soup.prettify())