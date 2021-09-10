"""
=====================
Get manga related stuff.
=====================
"""

import asyncio, aiohttp
from bs4 import BeautifulSoup
from AniManga.helpers.MangaHelpers import check_if_exists, format

async def req(link):
  async with aiohttp.ClientSession() as session:
    async with session.get(link) as resp:
      return await resp.content.read()

class Manga:
    """
    Manga class.
    """



    async def get_manga_json(self, manga: str) -> dict:
        """
        Get information on a manga.
        """
        manga = format(manga)
        r = await req("https://www.anime-planet.com/manga/" + f"{manga}")
        soup = BeautifulSoup(r, "html5lib")
        tags = soup.find_all("div", {"class": "tags"})
        rr = await req("https://www.anime-planet.com/manga/{}/reviews".format(manga))
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

            content_warning = soup.find_all("div", {"class": "tags tags--plain"})

            for x in content_warning:
                x = x.text.replace("\n", "").replace("Content Warning", "")
                warning_list.append(x)

            reviews = rsoup.find_all("div", {"class": "pure-1 userContent readMore"})
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

            dict = {}
            dict["title"] = soup.find("meta", property="og:title")["content"]
            dict["description"] = soup.find("meta", property="og:description")[
                "content"
            ]
            dict["url"] = soup.find("meta", property="og:url")["content"]
            dict["type"] = soup.find("meta", property="og:type")["content"]
            dict["size"] = soup.find("div", {"class": "pure-1 md-1-5"}).text.replace(
                "\n", ""
            )
            dict["year"] = soup.find("span", {"class": "iconYear"}).text.replace(
                "\n", ""
            )
            dict["rating"] = soup.find("div", {"class": "avgRating"}).text.replace(
                "\n", ""
            )
            dict["rank"] = rank
            dict["author"] = soup.find("meta", property="book:author")["content"]
            dict["author"] = dict["author"].replace(
                "https://www.anime-planet.com/people/", ""
            )
            dict["cover"] = soup.find("meta", property="og:image")["content"]
            dict["tags"] = tags_list
            dict["content warning"] = warning_list
            dict["characters"] = characters
            dict["reviews"] = reviews
            return dict
        else:
            raise ReferenceError("Could not find that Manga.")

    async def get_manga_description(self, manga: str) -> str:
        """
        Get manga description.
        """
        x = await self.get_manga_json(Manga, manga)
        try:
            return x["description"]
        except:
            raise ReferenceError("Could not find that Manga.")

    async def get_manga_url(self, manga: str) -> str:
        """
        Get Anime-Planet link of a manga.
        """
        x = await self.get_manga_json(Manga, manga)
        try:
            return x["url"]
        except:
            raise ReferenceError("Could not find that Manga.")

    async def get_manga_size(self, manga: str) -> str:
        """
        Get size of a manga.
        """
        x = await self.get_manga_json(Manga, manga)
        try:
            return x["size"]
        except:
            raise ReferenceError("Could not find that Manga.")

    async def get_manga_year(self, manga: str) -> str:
        """
        Get the years the manga ran.
        """
        x = await self.get_manga_json(Manga, manga)
        try:
            return x["year"]
        except:
            raise ReferenceError("Could not find that Manga.")

    async def get_manga_rating(self, manga: str) -> str:
        """
        Get rating of a manga according to Anime-Planet.
        """
        x = await self.get_manga_json(Manga, manga)
        try:
            return x["rating"]
        except:
            raise ReferenceError("Could not find that Manga.")

    async def get_manga_rank(self, manga: str) -> str:
        """
        Get rank of the manga according to Anime-Planet.
        """
        x = await self.get_manga_json(Manga, manga)
        try:
            return x["rank"]
        except:
            raise ReferenceError("Could not find that Manga.")

    async def get_manga_cover(self, manga: str) -> str:
        """
        Get cover image of manga.
        """
        x = await self.get_manga_json(Manga, manga)
        try:
            return x["cover"]
        except:
            raise ReferenceError("Could not find that Manga.")

    async def get_manga_author(self, manga: str) -> str:
        """
        Get author of a manga.
        """
        x = await self.get_manga_json(Manga, manga)
        try:
            return x["author"]
        except:
            raise ReferenceError("Could not find that Manga.")

    async def get_manga_tags(self, manga: str) -> list:
        """
        Get the tags of a manga.
        """

        x = await self.get_manga_json(Manga, manga)
        try:
            return x["tags"]
        except:
            raise ReferenceError("Could not find that Manga.")

    async def get_manga_content_warning(self, manga: str) -> list:
        """
        Get content warning of a manga.
        """
        x = await self.get_manga_json(Manga, manga)
        try:
            return x["content warning"]
        except:
            raise ReferenceError("Could not find that Manga.")

    async def get_manga_reviews(self, manga: str) -> list:
        """
        Get the reviews of a manga.
        """

        x = await self.get_manga_json(Manga, manga)

        try:
            return x["reviews"]
        except:
            raise ReferenceError("Could not find that Manga.")

    async def get_manga_characters(self, manga: str) -> list:
        """
        Get the characters of a manga.
        """
        manga = format(manga)
        r = await req(
            "https://www.anime-planet.com/manga/{}/characters".format(manga)
        )
        soup = BeautifulSoup(r, "html5lib")

        character_list = []

        characters = soup.find_all("a", {"class": "name"})

        for i in characters:
            character_list.append(i.text)

        try:
            return character_list
        except:
            raise ReferenceError("Could not find that Manga.")

    async def get_popular_manga(self) -> list:
        """
        Gets current popular manga according to Anime-Planet.
        """

        r = await req("https://www.anime-planet.com/manga/all")
        soup = BeautifulSoup(r, "html5lib")

        try:
            x = soup.find_all("ul", {"class": "cardDeck cardGrid"})

            list = []

            for ultag in x:
                for y in ultag.find_all("li"):
                    y = y.text.replace("Add to list ", "").replace("\n", "")
                    list.append(y)

            return list
        except:
            raise ReferenceError("Could not find that Manga.")

loop = asyncio.get_event_loop()
print("Running.")
print(loop.run_until_complete(Manga.get_popular_manga(Manga)))
