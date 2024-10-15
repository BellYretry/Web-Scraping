import requests
from bs4 import BeautifulSoup

# Genere les pages
def make_requests():
    pages = []
    num_page = 1
    for i in range(100):
        i = f"https://stggege.org/page{num_page}"
        r = requests.get(i)
        if r.status_code == 200:
            num_page += 1
            pages.append(i)
        else:
            print(f"Erreur 404 à l'url {i}")
            break
    return pages

# Fait la requete aux pages et recupere le nom des jeux de celle-ci
def requete(parone):
    pre_jeux = []
    requests_pages = requests.get(parone)
    soup = BeautifulSoup(requests_pages.content, "html.parser")

    #Scrap les données viser
    pages2jeux = soup.find('div', class_='games').text

    #Ajoute les resultat a la liste
    pre_jeux.append(pages2jeux)

    # Met au propre la liste
    jeux = [jeu for jeu in pre_jeux[0].split("\n") if jeu.strip()]
    print(jeux)
    return jeux

    # Indique le chemin de sorti pour le fichier
    chemin = r'C:\Users\CRABOUZE\Desktop\Stggege.txt'
    with open(chemin, "a", encoding="utf-8") as f:
        f.write(f"{jeux}")

# Fonction principale
def main():
    jeux_total = []
    pages = make_requests()
    for pg in pages:
        jeux = requete(parone=pg)
        jeux_total.extend(jeux)  # Ajout des jeux recupere à la liste totale
    print(f"Nombre total de jeux sur Stggege : {len(jeux_total)}")

# Je lance le script
if __name__ == '__main__':
    main()
