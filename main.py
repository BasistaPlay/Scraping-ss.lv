from rich.console import Console
import requests
from bs4 import BeautifulSoup
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt

table = Table(title="Audi")

table.add_column("Lapa", justify="right", style="red")
table.add_column("Cena", justify="right", style="cyan", no_wrap=True)
table.add_column("Modelis", justify="right", style="green")
table.add_column("Gads", justify="right", style="green")
table.add_column("Tilp.", justify="right", style="green")
table.add_column("Nobraukums", justify="right", style="green")
table.add_column("Modelis", justify="right", style="green")
table.add_column("Apraksts", style="magenta")

Link = Prompt.ask("Ierakstiet ss.lv vēlamo sludinājumu lapu")

nr = 1
while True:
    source = requests.get(Link + 'page'+str(nr)+'.html')
    soup = BeautifulSoup(source.text, "html.parser")
    for tr in soup.find_all("tr", id=lambda i: i and i.startswith("tr_")):
        tds = [
            text
            for td in tr.select("td")
            if (text := td.get_text(strip=True, separator=" "))
        ]
        # print some sample data:
        if tds:
            table.add_row(str(nr), tds[-1], tds[1], tds[2],
                          tds[3], tds[4], tds[5], tds[0])
    nr += 1
    console = Console()
    console.print(table)
    if nr == 70:
        break
input("Nospied Enter lai izietu.")
