from zip_processor import ZipProcessor
from PIL import Image
import json


class ScaleZip(ZipProcessor):
    """A class for scaling images inside archives."""

    def __init__(self, filename, size=(640, 480)):
        """
        Receives a desired size for the pictures (defaults to 640x480)
        and the archive name.
        :param filename: str
        :param size: tuple
        """
        super().__init__(filename)

        if isinstance(size, tuple) and size in ScaleZip.get_resolutions():
            self.res = size
        else:
            print("Defaulting to 640x480.")
            self.res = (640, 480)

    def process_files(self):
        """
        Scale each image in the directory to self.size.
        :return: None
        """
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize(self.res)
            scaled.save(str(filename))

    @staticmethod
    def get_resolutions():
        """
        Returns a set of all pixel resolutions from resolutions.json.
        :return: set
        """
        resolution_set = set()

        with open("resolutions.json", "r") as jsn:
            resolutions = json.load(jsn)
            for res in resolutions:
                resolution_set.add(tuple(resolutions[res]))

        return resolution_set
