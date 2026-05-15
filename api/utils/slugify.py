import unicodedata
import re
import os


def slugify(text):
    text = text.strip()

    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')

    text = text.lower()

    text = re.sub(r'[^a-z0-9]+', '-', text)

    text = text.strip('-')

    return text
def data_card():
    try:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        FILE_DIR = os.path.join(BASE_DIR, "file")

        conteudo = os.listdir(FILE_DIR)
        
        dados = []

        for x in conteudo:
            base = x.strip().replace(".csv", "")
            url = slugify(base)
            
            dados.append({
                "nome": base,
                "url_p": f"card/{url}"
            })
        
        return dados

    except Exception as e:
        print("Erro:", e)
        return []

def data_card_computer_architecture():
    try:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        DIR = os.path.join(BASE_DIR, "file", "Arquitetura de Computadores")
        
        conteudo = os.listdir(DIR)
        
        dados = []
    
        for x in conteudo:
                base = x.strip().replace(".csv", "")
                url = slugify(base)
                
                dados.append({
                    "nome": base,
                    "url_p": f"computer-architecture/{url}"
            })
        
        return dados

    except Exception as e:
        print("Erro:", e)
        return []

def data_read():
    dados = [
        {
            "nome": "Anatomia da Computação",
            "url_p": "read/anatomia-da-computacao-pdf"
        },
        {
            "nome": "Digital Data",
            "url_p": "read/digital-data-pdf"
        }
    ]
    
    return dados
