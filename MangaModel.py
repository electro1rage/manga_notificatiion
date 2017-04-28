
class Files:
	manga_followed_path = "manga_followed"
	manga_latest_path = "last_chapter"

class Manga:
	class Followed:
		def __init__(self):
			self.base_url = "http://mangafox.me/manga/"
		def add(self, manga_link):
			manga_wanted_file = open(Files().manga_followed_path, "a")
			manga_wanted_file.write(manga_link + '\n')
			manga_wanted_file.close()
		def add_name(self, manga_name):
			Manga.Followed().add(self.base_url + manga_name)
		def get(self):
			manga_wanted_file = open(Files().manga_followed_path)
			manga_wanted = manga_wanted_file.read().split()
			manga_wanted_file.close()
			return manga_wanted
	class Latest:
		def add_dict(self, manga_dict):
			manga_dict = dict(manga_dict)
			manga_latest_file = open(Files().manga_latest_path, "w")
			for key in manga_dict:
				manga_latest_file.write(str(key) + " " + str(manga_dict[key]) + "\n")
			manga_latest_file.close()
		def get(self):
			manga_latest_file = open(Files().manga_latest_path)
			read_dic = {}
			manga_latest = manga_latest_file.read()
			manga_list = manga_latest.split("\n")[0:-1]
			for manga in manga_list:
				manga_chapter_list = manga.split()
				read_dic[' '.join(str(x) for x in manga_chapter_list[0:-1])] = manga_chapter_list[-1]
			manga_latest_file.close()
			return read_dic
