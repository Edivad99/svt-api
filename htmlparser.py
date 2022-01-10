from bs4 import BeautifulSoup
from models.fermata import Fermata

class HtmlParser:

    @staticmethod
    def get_fermate(html_raw: str) -> list[Fermata]:
        soup = BeautifulSoup(html_raw, 'html.parser')

        fermate: list[Fermata] = []
        for td in soup.select('#col1 table tr td[title]'):
            fermate.append(Fermata(td.get('title').strip()))

        i = 0
        for tr in soup.select('#col2 table tr'):
            if(len(tr.contents) > 0): #Il tr non è vuoto
                for content in tr.contents:
                    fermate[i].add(content.text)
                i+=1
        return fermate