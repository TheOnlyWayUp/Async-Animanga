# Async-Animanga
## An Async/Aiohttp compatible  library.

Async-Animanga is an async ready web scraping library that returns Manga information from animeplanet. Hentai and Anime are not supported as of yet but will be soon.

## Installation
```py
python3 -m pip install Async-Animanga
>>> from Async_Animanga import Manga
```

#### What you can get
##### Manga
- Manga Author
- - `get_manga_author(self, manga: str)` String output.
- Manga Characters
- - `get_manga_characters(self, manga: str)` List output.
- Manga Content Warnings
- - `get_manga_content_warning(self, manga: str)` List output.
- Manga Cover (URL)
- - `get_manga_cover(self, manga: str)` String output.
- Manga Description
- - `get_manga_description(self, manga: str)` String output.
- All Manga Information as JSON (Use the functions instead)
- - `get_manga_json(self, manga: str)` Dictionary output.
- Manga Rank
- - `get_manga_rank(self, manga: str)` String output.
- Manga Rating
- - `get_manga_rating(self, manga: str)` String output.
- Manga Reviews
- - `get_manga_reviews(self, manga: str)` List output.
- Manga Size
- - `get_manga_size(self, manga: str)` String output.
- Manga Tags
- - `get_manga_tags(self, manga: str)` List output.
- Manga URL
- - `get_manga_url(self, manga: str)` String output.
- Manga Years (Years Manga was in Production)
- - `get_manga_year(self, manga: str)` String output.
- Popular Manga
- - `get_popular_manga(self)` List output.


Code and Response examples will be below.

## Authors:
- [Original library Author](https://github.com/centipede000/AniManga) - [Siddhant Kumar](https://github.com/centipede000)
- **CURRENT LIBRARY** - [Async Library Author - TheOnlyWayUp](https://github.com/TheOnlyWayUp)

## Acknowledgements
* [Non-Async library Author - Centipede000](https://github.com/centipede000)
* [Scraped site - Anime-Planet](https://animeplanet.com)

## Code Examples

#### Manga Author
```py
from Async-Animanga import Manga
loop = asyncio.get_event_loop()
print(loop.run_until_complete(Manga.get_manga_author(Manga, "bleach")))
```
`tite-kubo`
#### Manga Characters
```py
from Async-Animanga import Manga
loop = asyncio.get_event_loop()
print(loop.run_until_complete(Manga.get_manga_characters(Manga, "bleach")))
```
`['Ichigo KUROSAKI', 'Orihime INOUE', 'Renji ABARAI', 'Rukia KUCHIKI', 'Uryuu ISHIDA', 'Yasutora SADO', 'Byakuya KUCHIKI', 'Coyote STARRK', 'Dondochakka BILSTIN', 'Ganju SHIBA', 'Genryuusai YAMAMOTO', 'Gin ICHIMARU', 'Grimmjow JEAGERJAQUES', 'Hanatarou YAMADA', 'Hiyori SARUGAKI', 'Ikkaku MADARAME', 'Isane KOTETSU', 'Izuru KIRA', 'Juushiro UKITAKE', 'Kaname TOUSEN', 'Kenpachi ZARAKI', 'Kisuke URAHARA', 'Kon', 'Kugo GINJO', 'Marechiyo OMAEDA', 'Mayuri KUROTSUCHI', 'Momo HINAMORI', 'Neliel Tu ODELSCHWANCK', 'Nnoitra JIRUGA', 'Pesche GUATICHE'...]`
It actually returns a huge list, I shortened it here.
#### Manga Content Warning
```py
from Async-Animanga import Manga
loop = asyncio.get_event_loop()
print(loop.run_until_complete(Manga.get_manga_content_warning(Manga, "bleach")))
```
`['Violence']`
#### Manga Cover
```py
from Async-Animanga import Manga
loop = asyncio.get_event_loop()
print(loop.run_until_complete(Manga.get_manga_cover(Manga, "bleach")))
```
`https://www.anime-planet.com/images/manga/covers/178.jpg?t=1394840454`
#### Manga Description
```py
from Async-Animanga import Manga
loop = asyncio.get_event_loop()
print(loop.run_until_complete(Manga.get_manga_description(Manga, "bleach")))
```
`Ichigo Kurosaki&nbsp;is an average high school boy with a not-so-average ability to see spirits - something that hadn't affected his life much until a strange woman entered his room one day. Named Kuchiki Rukia, she's a shinigami who was sent from the spirit world to destroy a hollow - a dead-soul-turned-monster; and much to her surprise, Ichigo can see her. When the hollow suddenly attacks his family, Rukia intervenes and is injured in the process, leaving Ichigo to fight it himself. But when Rukia lends him her shinigami powers - which is forbidden - he inadvertently drains them away and has no way to return them. Now, Ichigo is a full-fledged...`
It returned the full description but I shortened it.
#### Manga JSON
```py
from Async-Animanga import Manga
loop = asyncio.get_event_loop()
print(loop.run_until_complete(Manga.get_manga_json(Manga, "bleach")))
```
`
#### Manga Rank
```py
from Async-Animanga import Manga
loop = asyncio.get_event_loop()
print(loop.run_until_complete(Manga.get_manga_rank(Manga, "bleach")))
```
`{'title': 'Bleach', 'description': "Ichigo Kurosaki&nbsp;is an average high school boy with a not-so-average ability to see spirits - something that hadn't affected his life much until a strange woman entered his room one day. Named Kuchiki Rukia, she's a shinigami who was sent from the spirit world to destroy a hollow - a dead-soul-turned-monster; and much to her surprise, Ichigo can see her. When the hollow suddenly attacks his family, Rukia intervenes and is injured in the process, leaving Ichigo to fight it himself. But when Rukia lends him`
It returned the full JSON, I shortened it.
#### Manga Rating
```py
from Async-Animanga import Manga
loop = asyncio.get_event_loop()
print(loop.run_until_complete(Manga.get_manga_rating(Manga, "bleach")))
```
`Rank #1,954`
#### Manga Reviews
```py
from Async-Animanga import Manga
loop = asyncio.get_event_loop()
print(loop.run_until_complete(Manga.get_manga_reviews(Manga, "bleach")))
```
`['Story:\n', "I love Bleach. I think it has some great story arcs, awesome characters and some cool action scenes. However, amongst that is the 9 volume wait for the main plot to start (athough it's well worth the wait), some seriously underdeveloped characters and that stupid but necessary story arc in volumes 49-54.\n", 'Okay... I need to get my thoughts down on this series. I\'ve been a Naruto fan for the past six years and only this year, 2013, did I decide to sit down and read the Bleach manga. I thought "Now I\'d be the biggest goddamn hypocrite if I said Bleach sucked ass without ever perusing the source material". Never mind that I had been saying that the whole time I had been a Naruto fan.\n', '*THIS REVIEW IS BASED ON CHAPTERS 1-581*\n', 'Bleach\n']`
#### Manga Size
```py
from Async-Animanga import Manga
loop = asyncio.get_event_loop()
print(loop.run_until_complete(Manga.get_manga_size(Manga, "bleach")))
```
`Vol: 74; Ch: 686`
#### Manga Tags
```py
from Async-Animanga import Manga
loop = asyncio.get_event_loop()
print(loop.run_until_complete(Manga.get_manga_tags(Manga, "bleach")))
```
`['Action', 'Adventure', 'Comedy', 'Drama', 'Shounen', 'Afterlife', 'Ghosts', 'Shinigami', 'Supernatural', 'Adapted to Anime', 'Violence']`
#### Manga URL
```py
from Async-Animanga import Manga
loop = asyncio.get_event_loop()
print(loop.run_until_complete(Manga.get_manga_url(Manga, "bleach")))
```
`https://www.anime-planet.com/manga/bleach`
#### Manga Year
```py
from Async-Animanga import Manga
loop = asyncio.get_event_loop()
print(loop.run_until_complete(Manga.get_manga_year(Manga, "bleach")))
```
`2002 - 2016`
#### Popular Manga
```py
from Async-Animanga import Manga
loop = asyncio.get_event_loop()
print(loop.run_until_complete(Manga.get_popular_manga(Manga, "bleach")))
```
`['Solo Leveling', 'The Beginning After the End', 'Tokyo Revengers', 'Eleceed', 'Haikyuu!!', 'One Piece', 'Here U Are', "JoJo's Bizarre Adventure Part 7: Steel Ball Run", 'Berserk', 'Here U Are - Specials', 'Toilet-Bound Hanako-kun', 'Semantic Error', 'That Time I Got Reincarnated as a Slime ', 'I Shall Master This Family', '19 Days', "Heaven Official's Blessing", 'Who Made Me a Princess', 'The Master of Diabolism', 'Fullmetal Alchemist', 'I Had That Same Dream Again', 'Given', 'The Founder of Diabolism (Novel)'...]`
It returned the full list, I shortened it.