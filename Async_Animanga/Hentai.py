"""
=====================
Get hentai/doujin related stuff.
=====================
"""

import aiohttp, asyncio
from bs4 import BeautifulSoup

async def req(link):
  async with aiohttp.ClientSession() as session:
    async with session.get(link) as resp:
      return await resp.content.read()

class Doujin:
    """
    Scrapes nhentai.net for doujin information.
    """
    def __init__(self, verbose=False):
        """
        __init__ function.
        """
        self.verbose = verbose
    
    async def get_doujin_json(self, code: int) -> dict:
        """Get information on a doujin from nhentai.net in dict/json format.
        Args:
            code (int): the ~6 digit code used to uniquely identify doujins.
        Returns:
            dict: dict/json with doujin information (title, cover url, tags, description, languages, type, pages, upload time, favorites).
        """
        code = str(code)
        r = await req("https://nhentai.net/" + "g/" + code)
        s = BeautifulSoup(r, "html5lib")
        if s.find("div",{"class":"container error"}):
            return "Error: Doujin '{}' most likely doesnt exist.".format(code) if not self.verbose else "Error: Doujin '{}' most likely doesnt exist. Possible fixes might be rechecking the name.".format(code)
        else:
            doujin_dict = {}
            doujin_dict["title"] = s.find("meta", property="og:title")["content"]
            doujin_dict["cover"] = s.find("meta", property="og:image")["content"]
            doujin_dict["tags"] = s.find("meta",attrs={"name":"twitter:description"})["content"].split(", ")
            doujin_dict["description"] = s.find("meta", attrs={"name":"description"})["content"]
            other_info = s.find_all("div",{"class":"tag-container field-name"})
            other_info_list = []
            for i in other_info:
                i = i.find_all("span",{"class":"name"})
                other_info_list.append(i)
            doujin_dict["artist"] = other_info_list[1][0].text
            languages = []
            for i in other_info_list[2]:
                languages.append(i.text)
            doujin_dict["languages"] = languages
            doujin_dict["type"] = other_info_list[3][0].text
            doujin_dict["pages"] = other_info_list[4][0].text
            for i in other_info:
                i = i.find("time")
                if i:
                    uploaded_time = i.text
            doujin_dict["uploaded"] = uploaded_time
            doujin_dict["favorites"] = s.find("div",{"class":"buttons"}).find("span",{"class":"nobold"}).text.replace("Favorite","").replace("(","").replace(")","")
            return doujin_dict

    async def get_doujin_title(self, code: str) -> str:
        r = await req("https://nhentai.net/" + "g/" + code)
        s = BeautifulSoup(r, "html5lib")
        return s.find("meta", property="og:title")["content"]

    async def get_doujin_cover(self, code: str) -> str:
        r = await req("https://nhentai.net/" + "g/" + code)
        s = BeautifulSoup(r, "html5lib")
        return s.find("meta", property="og:image")["content"]

    async def get_doujin_tags(self, code: str) -> str:
        r = await req("https://nhentai.net/" + "g/" + code)
        s = BeautifulSoup(r, "html5lib")
        return s.find("meta",attrs={"name":"twitter:description"})["content"].split(", ")

    async def get_doujin_description(self, code: str) -> str:
        r = await req("https://nhentai.net/" + "g/" + code)
        s = BeautifulSoup(r, "html5lib")
        return s.find("meta", attrs={"name":"description"})["content"]

    async def get_doujin_artist(self, code: str) -> str:
        r = await self.get_doujin_json(self, code)
        return r["artist"]

    async def get_doujin_languages(self, code: str) -> str:
        r = await self.get_doujin_json(self, code)
        return r["languages"]

    async def get_doujin_type(self, code: str) -> str:
        r = await self.get_doujin_json(self, code)
        return r["type"]

    async def get_doujin_pages(self, code: str) -> str:
        r = await self.get_doujin_json(self, code)
        return r["pages"]

    async def get_doujin_uploaded(self, code: str) -> str:
        r = await self.get_doujin_json(self, code)
        return r["uploaded"]

    async def get_doujin_favourites(self, code: str) -> str:
        r = await self.get_doujin_json(self, code)
        return r["favourites"]
