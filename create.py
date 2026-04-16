import os
import unicodedata
import re


def slugify(text):
    text = text.strip()

    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')

    text = text.lower()

    text = re.sub(r'[^a-z0-9]+', '-', text)

    text = text.strip('-')

    return text

conteudo = os.listdir("./api/file")
def ht():
    with open("./api/templates/in.html", "r") as file:
        fil = file.read()
    for x in conteudo:
        name = x.replace(".csv", "").replace(" ", "-")\
            .replace("ç", "c").replace("ã", "a").replace("é", "e")\
                .replace("à", "a").lower()
        with open(f"./templates/{name}.html", "w") as f:
            f.write(fil)
            
            
def func():
    with open(f"./func.txt", "a", encoding="utf-8") as f:
        for x in conteudo:
            base = x.replace(".csv", "")
            n = slugify(base)
                
            #name = n.replace(".csv", "").replace(" ", "-").lower()
            f.write(f"""@app.route('/{n}/')
def {n.replace("-", "_")}():
    list_quest = []
    with open("./api/file/{x}", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('{n}.html', quest=list_quest)""" + "\n\n")
            
func()