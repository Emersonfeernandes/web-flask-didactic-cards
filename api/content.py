import os
import unicodedata
import re

conteudo = os.listdir("api/file")

def slugify(text):
    text = text.strip()

    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')

    text = text.lower()

    text = re.sub(r'[^a-z0-9]+', '-', text)

    text = text.strip('-')

    return text

def content():
    content_list = []
    for x in conteudo:
        base = x.replace(".csv", "")
        n = slugify(base)
        
        content_list.append([n, x])
        
    return content_list