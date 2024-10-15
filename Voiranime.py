import requests
from bs4 import BeautifulSoup

def get_info(url, episode_anime):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    episode = soup.find('select', class_='c-selectpicker selectpicker_chapter selectpicker single-chapter-select').text.strip()
    episode_anime.append(episode)
    nom = soup.find('a',  href="https://v5.voiranime.com/anime/genjitsu-shugi-yuusha-no-oukoku-saikenki/").text.strip()
    return nom

def get_update(liste_episode_anime, url_user, simplified_url):
    new_liste_episode_anime = []
    r = requests.get(url_user)
    soup = BeautifulSoup(r.content, "html.parser")
    episode = soup.find('select', class_='c-selectpicker selectpicker_chapter selectpicker single-chapter-select').text.strip()
    new_liste_episode_anime.append(episode)
    nom = soup.find('a', href=f"{simplified_url}").text.strip()

    if liste_episode_anime == new_liste_episode_anime:
        pass
    else:
        print(f"L'épisode  de {nom} vient de sortir\n voici le lien pour allez le voir ")
        liste_episode_anime.extend(new_liste_episode_anime)
        print(new_liste_episode_anime)


def simplify_url(url_user):
    pre_simplified_url = url_user.split('/')

    base_url_parts = pre_simplified_url[:5]

    simplified_url = '/'.join(base_url_parts) + '/'
    print(simplified_url)

    return simplified_url


def main():
    episode_anime = []
    url = "https://v5.voiranime.com/anime/genjitsu-shugi-yuusha-no-oukoku-saikenki/genjitsu-shugi-yuusha-no-oukoku-saikenki-18-vostfr/"
    nom = get_info(url, episode_anime)
    get_info(url, episode_anime)
    liste_episode_anime = episode_anime[0].split("\n")
    print(f"Nouvel épisode de : {nom} \nAu total {len(liste_episode_anime)} épisodes")
    url_user = "https://v5.voiranime.com/anime/one-piece/one-piece-1109-vostfr/"
    simplified_url = simplify_url(url_user)
    get_update(liste_episode_anime, url_user, simplified_url)

if __name__ == '__main__':
    main()