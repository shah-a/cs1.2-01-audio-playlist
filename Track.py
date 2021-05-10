"""Node class."""

class Track:

    def __init__(self, title):
            self.__title = title.title()
            self.__next_track = None

    def get_title(self):
        return self.__title

    def get_next_track(self):
        return self.__next_track

    def set_title(self, title):
        self.__title = title.title()

    def set_next_track(self, next_title):
        self.__next_track = next_title.title()

    def __str__(self):
        return self.__title

    def __repr__(self):
        return f"{self.__title} -> {self.__next_track}"
