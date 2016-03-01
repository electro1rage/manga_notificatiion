import datetime
import requests
import time
from MangaModel import Manga
from bs4 import BeautifulSoup


class MangaFox:
	def __init__(self):
		self.base_url = "http://mangafox.me/manga/"
	def get_latest_manga(self, manga):
		html_file = requests.get(self.base_url + manga)
		ret_dict = {}
		if html_file.status_code == 200:
			ret_dict["status"] = 200
			html_doc = html_file.text
			soup = BeautifulSoup(html_doc, "html.parser")
			last_chapter_tag = soup.find("a", {"class":"tips"})
			last_chapter_tag = str(last_chapter_tag)
			soup = BeautifulSoup(last_chapter_tag, "html.parser")
			ret_dict["last_chapter_text"] = str(soup.get_text())
			ret_dict["last_chapter_link"] = str(soup.find("a").get("href"))
			return ret_dict
		ret_dict["status"] = 404
		return ret_dict


manga_followed = list(Manga().Followed().get())
manga_latest = dict(Manga().Latest().get())

while 1:
	print(datetime.datetime.now())
	manga_fox = MangaFox()
	got_new = 0
	for manga in manga_followed:
		last_chapter_dict = dict(manga_fox.get_latest_manga(manga))
		if last_chapter_dict["status"] == 404:
			continue
		last_chapter_text = last_chapter_dict["last_chapter_text"]
		last_chapter_link = last_chapter_dict["last_chapter_link"]
		last_chapter = last_chapter_text.split()
		last_chapter_name = " ".join(str(x) for x in last_chapter[0:-1])
		last_chapter_number = int(last_chapter[-1])
		if str(manga_latest.get(last_chapter_name, "NULL")) != str(last_chapter_number):
			manga_latest[last_chapter_name] = last_chapter_number
			print("new chapter!!! {} from Manga {}, link {}".format(last_chapter_number, last_chapter_name, last_chapter_link))
			got_new = 1
	if got_new == 1:
		Manga().Latest().add_dict(manga_latest)
		input("Lucky you found new Manga, click enter to continue!!")
	time.sleep(60)







