import aiohttp, asyncio#, urllib3
from bs4 import BeautifulSoup as bs
from helpers.AnimeHelpers import _format

async def req(link):
  async with aiohttp.ClientSession() as session:
    async with session.get(link) as resp:
      return await resp.content.read()

class Anime:
  def __init__(self) -> None:
      self.base_url = "https://www.anime-planet.com/anime/"
  async def get_anime_json(self, anime:str=None) -> dict:
    r = await req(self.base_url+ + _format(anime))
    s = bs(r, "html5lib")
    tags = s.find_all("div",{"class":"tags"})
    tags_list = []

    for x in tags:
      x = x.find_all("a")
      for y in x:
        y = y.text.replace("\n","")
        tags_list.append(y)
    section_bar = s.find("section",{"class":"pure-g entryBar"})
    _div = section_bar.find_all("div",{"class":"pure-1 md-1-5"})
    _section_bar_list = []
    for y in _div:
      y = y.text.replace("\n","")
      _section_bar_list.append(y)
    r = await req(f"https://www.anime-planet.com/anime/{_format(anime)}/reviews")
    s = bs(r,"html5lib")
    review = s.find_all("div",{"class":"pure-1 userContent readMore"})
    review_list = []
    for x in review:
      review_list.append(x.text)
    anime_dict = {}
    anime_dict["title"] = s.find("meta",property="og:title")["content"]
    anime_dict["description"] = s.find("meta",property="og:description")["content"]
    anime_dict["keywords"] = s.find("meta", attrs={"name":"keywords"})["content"].split(", ")
    anime_dict["tags"] = tags_list
    anime_dict["cover"] = s.find("meta",property="og:image")["content"]
    anime_dict["episodes"] = _section_bar_list[0]
    anime_dict["rank"] = _section_bar_list[4]
    anime_dict["rating"] = _section_bar_list[3]
    anime_dict["reviews"] = review_list
    anime_dict["uploaded"] = _section_bar_list[2]
    anime_dict["studio"] = _section_bar_list[1]
  async def get_anime_title(self, anime:str=None) -> str:
    r = await req(self.base_url+ + _format(anime))
    s = bs(r, "html5lib") 
    return s.find("meta",property="og:title")["content"]
  async def get_anime_description(self, anime:str=None) -> str:
    r = await req(self.base_url+ + _format(anime))
    s = bs(r, "html5lib") 
    return s.find("meta",property="og:description")["content"]
  async def get_anime_keywords(self, anime:str=None) -> str:
    r = await req(self.base_url+ + _format(anime))
    s = bs(r, "html5lib") 
    return s.find("meta", attrs={"name":"keywords"})["content"].split(", ")
  async def get_anime_tags(self, anime:str=None) -> list:
    r = await req(self.base_url+ + _format(anime))
    s = bs(r, "html5lib")
    tags = s.find_all("div",{"class":"tags"})
    tags_list = []
    for x in tags:
      x = x.find_all("a")
      for y in x:
        y = y.text.replace("\n","")
        tags_list.append(y)  
    return tags_list
  async def get_anime_episodes(self, anime:str=None) -> int:
    r = await req(self.base_url+ + _format(anime))
    s = bs(r, "html5lib")
    section_bar = s.find("section",{"class":"pure-g entryBar"})
    _div = section_bar.find_all("div",{"class":"pure-1 md-1-5"})
    _section_bar_list = []
    for y in _div:
        y = y.text.replace("\n","")
        _section_bar_list.append(y)
    return section_bar[0]
  async def get_anime_studio(self, anime:str=None) -> int:
    r = await req(self.base_url+ + _format(anime))
    s = bs(r, "html5lib")
    section_bar = s.find("section",{"class":"pure-g entryBar"})
    _div = section_bar.find_all("div",{"class":"pure-1 md-1-5"})
    _section_bar_list = []
    for y in _div:
        y = y.text.replace("\n","")
        _section_bar_list.append(y)
    return section_bar[1]
  async def get_anime_uploaded(self, anime:str=None) -> int:
    r = await req(self.base_url+ + _format(anime))
    s = bs(r, "html5lib")
    section_bar = s.find("section",{"class":"pure-g entryBar"})
    _div = section_bar.find_all("div",{"class":"pure-1 md-1-5"})
    _section_bar_list = []
    for y in _div:
        y = y.text.replace("\n","")
        _section_bar_list.append(y)
    return section_bar[2]
  async def get_anime_rating(self, anime:str=None) -> int:
    r = await req(self.base_url+ + _format(anime))
    s = bs(r, "html5lib")
    section_bar = s.find("section",{"class":"pure-g entryBar"})
    _div = section_bar.find_all("div",{"class":"pure-1 md-1-5"})
    _section_bar_list = []
    for y in _div:
        y = y.text.replace("\n","")
        _section_bar_list.append(y)
    return section_bar[3]
  async def get_anime_rank(self, anime:str=None) -> int:
    r = await req(self.base_url+ + _format(anime))
    s = bs(r, "html5lib")
    section_bar = s.find("section",{"class":"pure-g entryBar"})
    _div = section_bar.find_all("div",{"class":"pure-1 md-1-5"})
    _section_bar_list = []
    for y in _div:
        y = y.text.replace("\n","")
        _section_bar_list.append(y)
    return section_bar[4]
  async def get_anime_cover(self, anime:str=None) -> str:
    r = await req(self.base_url+ + _format(anime))
    s = bs(r, "html5lib")
    return s.find("meta",property="og:image")["content"]
  async def get_anime_url(self, anime:str=None) -> str:
    r = await req(self.base_url+ + _format(anime))
    s = bs(r, "html5lib")
    return s.find("meta",property="og:url")["content"]
  async def get_anime_reviews(self, anime:str) -> list:
    r = await req(self.base_url+ + _format(anime))
    s = bs(r, "html5lib")
    review = s.find_all("div",{"class":"pure-1 userContent readMore"})
    review_list = []
    for x in review:
      review_list.append(x.text)
    return review_list

  


