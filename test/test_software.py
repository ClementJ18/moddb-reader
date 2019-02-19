import unittest
import moddb

class TestSoftware(unittest.TestCase):
    def setUp(self):
        self.software = moddb.pages.Software(moddb.soup(getattr(self, "url", "https://www.moddb.com/software/project-neptune-vr")))

    def test_get_articles(self):
        articles = self.software.get_articles()
        self.software.get_articles(4)
        self.software.get_articles(category=moddb.ArticleType.news)

        for article in articles:
            article.parse()

    def test_get_comments(self):
        self.software.get_comments()
        self.software.get_comments(4)

    def test_get_files(self):
        files = self.software.get_files()
        self.software.get_files(4)
        self.software.get_files(category=moddb.FileCategory.demo)

        for file in files:
            file.parse()

    def test_get_games(self):
        games = self.software.get_games()
        self.software.get_games(3)

        for game in games:
            game.parse()

    def test_get_hardware(self):
        hardwares = self.software.get_hardware()
        self.software.get_hardware(3)

        for hardware in hardwares:
            hardware.parse()

    def test_get_images(self):
        images = self.software.get_images()

        for image in images[:10]:
            image.parse()

    def test_get_reviews(self):
        self.software.get_reviews()
        self.software.get_reviews(3)

    def test_get_software(self):
        softwares = self.software.get_software()
        self.software.get_software(3)

        for software in softwares:
            software.parse() 

    def test_get_tutorials(self):
        tutorials = self.software.get_tutorials()
        self.software.get_tutorials(3)
        self.software.get_tutorials(difficulty=moddb.Difficulty.basic)

        for tutorial in tutorials:
            tutorial.parse()

    def test_get_videos(self):
        videos = self.software.get_videos()

        for video in videos:
            video.parse()
