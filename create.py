import os

conteudo = os.listdir("./file")
def ht():
    with open("./templates/in.html", "r") as file:
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
            n = x.replace("ç", "c").replace("ã", "a").replace("é", "e").replace("à", "a")
            name = n.replace(".csv", "").replace(" ", "-").lower()
            f.write(f"""@app.route('/{name}/')
    def {n.replace(".csv", "").replace(" ", "_").lower()}():
        list_quest = []
        with open("./file/{x}", newline='', encoding="utf-8") as f:
            file = csv.reader(f)
            for row in file:
                list_quest.append(row)
        return render_template('{name}.html', quest=list_quest)""" + "\n\n")
            
func()