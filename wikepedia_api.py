import requests
from bs4 import BeautifulSoup

def get_wikipedia_intro_and_description(title):
    base_url = "https://en.wikipedia.org/wiki/" + title.replace(" ", "_")
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Finding the intro paragraph
    paragraphs= soup.find('div', class_="mw-content-ltr mw-parser-output").find_all('p')
    mylst=[]
    for i in range(2,10):
        intro_paragraph = paragraphs[i] if paragraphs else None
        intro_text= intro_paragraph.text.strip() if intro_paragraph else "Not available"
        mylst.append(intro_text)

    return mylst[0],mylst[1],mylst[2],mylst[3],mylst[4],mylst[5],mylst[6],mylst[7]


