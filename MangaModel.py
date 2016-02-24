import urllib.request
from bs4 import BeautifulSoup

def get_latest_manga(manga_name):
	manga_fox_url = "http://mangafox.me/manga/"
	manga_url = manga_fox_url + manga_name + ""
	print(manga_url)
	html_file = urllib.request.urlopen(manga_url)
	html_doc = html_file.read()
	soup = BeautifulSoup(html_doc, "html.parser")
	last_chapter_link = soup.find("a", {"class":"tips"})
	last_chapter_name = last_chapter_link.get_text()
	return last_chapter_name


last_chapter = get_latest_manga("chihayafuru")

last_chapter_number = last_chapter.split()[-1]
