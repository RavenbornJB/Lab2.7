from urllib.request import urlopen
from time import time, sleep


class AbstractPage:

    def __init__(self, url):
        self.url = url
        self._content = None


class WebPage(AbstractPage):

    TIME_DELTA = 10

    def __init__(self, url):
        super().__init__(url)
        self.load_time = 0

    @property
    def content(self):
        tm = time()
        if not self._content or tm - self.load_time > WebPage.TIME_DELTA:
            print("Retrieving New Page...")
            self.load_time = tm
            self._content = urlopen(self.url).read()
        return self._content
