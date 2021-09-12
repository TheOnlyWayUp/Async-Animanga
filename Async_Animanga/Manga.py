"""
=====================
Get manga related stuff.
=====================
"""

import asyncio, aiohttp
from bs4 import BeautifulSoup
from AniManga.helpers.MangaHelpers import check_if_exists
from AniManga.helpers.MangaHelpers import format as format_manga_name

async def req(link):
  async with aiohttp.ClientSession() as session:
    async with session.get(link) as resp:
      return await resp.content.read()

class Manga:
    """
    Manga class.
    """

    def __init__(self, verbose=False):
        """
        __init__
        """
        self.base_manga_url = "https://www.anime-planet.com/manga/"
        self.base_manga_reviews = "https://www.anime-planet.com/manga/{}/reviews"
        self.base_manga_tags = "https://www.anime-planet.com/manga/"
        self.verbose = verbose

    async def get_manga_json(self, manga: str) -> dict:
        """Get information on a manga.
        Args:
            manga (str): manga name you want to search for.
        Returns:
            dict: dict with information on the manga.
        """
        manga = format_manga_name(manga)
        r = await req(self.base_manga_url + f"{manga}")
        soup = BeautifulSoup(r, "html5lib")
        tags = soup.find_all("div", {"class": "tags"})
        rr = await req(self.base_manga_reviews.format(manga))
        rsoup = BeautifulSoup(rr, "html5lib")

        if check_if_exists(manga):

            rank = soup.find_all("div", {"class": "pure-1 md-1-5"})
            for x in rank:
                if x.text.startswith("\nRank"):
                    rank = x.text.replace("\n", "")

            tags_list = []

            for x in tags:
                x = x.find_all("li")
                for z in x:
                    z = z.text.replace("\n", "")
                    tags_list.append(z)

            characters = []
            for x in soup.find_all(
                "strong", {"class": "CharacterCard__title rounded-card__title"}
            ):
                characters.append(x.text)

            characters = characters[:-1]

            warning_list = []

            content_warning = soup.find_all(
                "div", {"class": "tags tags--plain"})

            for x in content_warning:
                x = x.text.replace("\n", "").replace("Content Warning", "")
                warning_list.append(x)

            reviews = rsoup.find_all(
                "div", {"class": "pure-1 userContent readMore"})
            review_list = []

            for x in reviews:
                review_list.append(x)

            reviews = []

            for x in review_list:
                string = ""
                while True:
                    try:
                        x = x.find("p")
                        x = x.getText()
                        string += f"{x}\n"
                    except:
                        break

                reviews.append(string)

            manga_dict = {}
            manga_dict["title"] = soup.find("meta", property="og:title")["content"]
            manga_dict["description"] = soup.find("meta", property="og:description")[
                "content"
            ]
            manga_dict["url"] = soup.find("meta", property="og:url")["content"]
            manga_dict["type"] = soup.find("meta", property="og:type")["content"]
            manga_dict["size"] = soup.find("div", {"class": "pure-1 md-1-5"}).text.replace(
                "\n", ""
            )
            manga_dict["year"] = soup.find("span", {"class": "iconYear"}).text.replace(
                "\n", ""
            )
            manga_dict["rating"] = soup.find("div", {"class": "avgRating"}).text.replace(
                "\n", ""
            )
            manga_dict["rank"] = rank
            manga_dict["author"] = soup.find(
                "meta", property="book:author")["content"]
            manga_dict["author"] = manga_dict["author"].replace(
                "https://www.anime-planet.com/people/", ""
            )
            manga_dict["cover"] = soup.find("meta", property="og:image")["content"]
            manga_dict["tags"] = tags_list
            manga_dict["content warning"] = warning_list
            manga_dict["characters"] = characters
            manga_dict["reviews"] = reviews
            try:
                return manga_dict
            except:
                return "We could not find that. Manga is most likely not available."
        else:
            return "We could not find that."

    async def get_manga_description(self, manga: str) -> str:
        """Gets description of a manga.
        Args:
            manga (str): manga for which description you need.
        Returns:
            str: description of the manga.
        """
        manga = format_manga_name(manga)
        r = await req(self.base_manga_url + f"{manga}")

        if check_if_exists(manga):
            soup = BeautifulSoup(r, "html5lib")
            return soup.find("meta", property="og:description")["content"]
        else:
            return "Manga could not be found, it most likely doesnt exist."

    async def get_manga_url(self, manga: str) -> str:
        """Get Anime-Planet URL of a manga.
        Args:
            manga (str): manga you want to search for.
        Returns:
            str: Anime-Planet URL.
        """
        manga = format_manga_name(manga)
        r = await req(self.base_manga_url + f"{manga}")

        if check_if_exists(manga):
            soup = BeautifulSoup(r, "html5lib")
            return soup.find("meta", property="og:url")["content"]
        else:
            return "Manga could not be found, it most likely doesnt exist."

    async def get_manga_size(self, manga: str) -> str:
        """Get the chapters/volume of a manga.
        Args:
            manga (str): manga you want to search for.
        Returns:
            str: chapters/volume numbers.
        """
        manga = format_manga_name(manga)
        r = await req(self.base_manga_url + f"{manga}")

        if check_if_exists(manga):
            soup = BeautifulSoup(r, "html5lib")
            return soup.find("div", {"class": "pure-1 md-1-5"}).text.replace("\n", "")
        else:
            return "Manga could not be found, it most likely doesnt exist."

    async def get_manga_year(self, manga: str) -> str:
        """Get the years a manga ran.
        Args:
            manga (str): manga you want to search for.
        Returns:
            str: years the manga ran.
        """
        manga = format_manga_name(manga)
        r = await req(self.base_manga_url + f"{manga}")

        if check_if_exists(manga):
            soup = BeautifulSoup(r, "html5lib")
            return soup.find("span", {"class": "iconYear"}).text.replace("\n", "")
        else:
            return "Manga could not be found, it most likely doesnt exist."

    async def get_manga_rating(self, manga: str) -> str:
        """Get the rating of a manga
        Args:
            manga (str): manga you want to search for.
        Returns:
            str: the rating.
        """
        manga = format_manga_name(manga)
        r = await req(self.base_manga_url + f"{manga}")

        if check_if_exists(manga):
            soup = BeautifulSoup(r, "html5lib")
            return soup.find("div", {"class": "avgRating"}).text.replace("\n", "")
        else:
            return "Manga could not be found, it most likely doesnt exist."

    async def get_manga_rank(self, manga: str) -> str:
        """Get the rank of a manga.
        Args:
            manga (str): manga you want to search for.
        Returns:
            str: the rank.
        """
        manga = format_manga_name(manga)
        r = await req(self.base_manga_url + f"{manga}")

        if check_if_exists(manga):
            soup = BeautifulSoup(r, "html5lib")
            rank = soup.find_all("div", {"class": "pure-1 md-1-5"})
            for x in rank:
                if x.text.startswith("\nRank"):
                    rank = x.text.replace("\n", "")
            return rank
        else:
            return "Manga could not be found, it most likely doesnt exist."

    async def get_manga_cover(self, manga: str) -> str:
        """Get the cover image url of a manga.
        Args:
            manga (str): manga you want to search for.
        Returns:
            str: cover image url. 
        """
        manga = format_manga_name(manga)
        r = await req(self.base_manga_url + f"{manga}")

        if check_if_exists(manga):
            soup = BeautifulSoup(r, "html5lib")
            return soup.find("meta", property="og:image")["content"]
        else:
            return "Manga could not be found, it most likely doesnt exist."
        

    async def get_manga_author(self, manga: str) -> str:
        """Get the author of a manga.
        Args:
            manga (str): manga you want to search for.
        Returns:
            str: author.
        """
        manga = format_manga_name(manga)
        r = await req(self.base_manga_url + f"{manga}")

        if check_if_exists(manga):
            soup = BeautifulSoup(r, "html5lib")
            author = soup.find("meta", property="book:author")["content"]
            author = author.replace("https://www.anime-planet.com/people/","")
            return author
        else:
            return "Manga could not be found, it most likely doesnt exist."

    async def get_manga_tags(self, manga: str) -> list:
        """Get the tags of a manga.
        Args:
            manga (str): manga you want to search for.
        Returns:
            list: tags of the manga.
        """
        manga = format_manga_name(manga)
        r = await req(self.base_manga_url + f"{manga}")

        if check_if_exists(manga):
            soup = BeautifulSoup(r, "html5lib")
            tags = soup.find_all("div", {"class": "tags"})
            tags_list = []

            for x in tags:
                x = x.find_all("li")
                for z in x:
                    z = z.text.replace("\n", "")
                    tags_list.append(z)
            return tags_list
        else:
            return "Manga could not be found, it most likely doesnt exist."

    async def get_manga_content_warning(self, manga: str) -> list:
        """Get the content warning of a manga.
        Args:
            manga (str): manga you want to search for.
        Returns:
            list: content warning.
        """
        manga = format_manga_name(manga)
        r = await req(self.base_manga_url + f"{manga}")

        if check_if_exists(manga):
            soup = BeautifulSoup(r, "html5lib")
            warning_list = []

            content_warning = soup.find_all(
                "div", {"class": "tags tags--plain"})

            for x in content_warning:
                x = x.text.replace("\n", "").replace("Content Warning", "")
                warning_list.append(x)

            return warning_list
        else:
            return "Manga could not be found, it most likely doesnt exist."

    async def get_manga_reviews(self, manga: str) -> list:
        """Get the reviews of a manga.
        Args:
            manga (str): manga you want to search for.
        Returns:
            list: reviews of the manga.
        """
        manga = format_manga_name(manga)
        r = await req(self.base_manga_url + f"{manga}")

        if check_if_exists(manga):
            rr = await req(self.base_manga_reviews.format(manga))
            rsoup = BeautifulSoup(rr, "html5lib")
            reviews = rsoup.find_all(
                "div", {"class": "pure-1 userContent readMore"})
            
            review_list = []

            for x in reviews:
                review_list.append(x)

            reviews = []

            for x in review_list:
                string = ""
                while True:
                    try:
                        x = x.find("p")
                        x = x.getText()
                        string += f"{x}\n"
                    except:
                        break

                reviews.append(string)
            return reviews
        else:
            return "Manga could not be found, it most likely doesnt exist."

    async def get_manga_characters(self, manga: str) -> list:
        """Get the characters of a manga.
        Args:
            manga (str): manga you want to search for.
        Returns:
            list: characters.
        """
        manga = format_manga_name(manga)

        r = await req(
            "https://www.anime-planet.com/manga/{}/characters".format(manga)
        )
        soup = BeautifulSoup(r, "html5lib")
        
        try:
            character_list = []
            characters = soup.find_all("a", {"class": "name"})
            for i in characters:
                character_list.append(i.text)
            
            return character_list
        except:
            return "We could not find characters from that manga, manga most likely doesn't exist."

    async def get_popular_manga(self) -> list:
        """Get currently popular manga.
        Args:
            manga (str): manga you want to search for.
        Returns:
            list: popular manga.
        """
        r = await req("https://www.anime-planet.com/manga/all")
        soup = BeautifulSoup(r, "html5lib")

        try:
            x = soup.find_all("ul", {"class": "cardDeck cardGrid"})

            popular_mangas = []

            for ultag in x:
                for y in ultag.find_all("li"):
                    y = y.text.replace("Add to list ", "").replace("\n", "")
                    popular_mangas.append(y)
        except Exception as ex:
            return ex
