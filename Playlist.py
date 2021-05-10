"""LinkedList class."""

from Track import Track

class Playlist:
    def __init__(self):
        self.__first_track = None
        # self.__len = 0

    def add_track(self, title):
        temp = Track(title)
        temp.set_next_track(self.__first_track)
        self.__first_track = temp
        # self.__len += 1

    def find_track(self, title):
        current = self.__first_track
        index = -1
        found = False
        while current != None:
            index += 1
            if current.get_title().lower() == title.lower():
                found = True
                break
            current = current.get_next_track()
        return index if found else -1

    def remove_track(self, title):
        current = self.__first_track
        previous = None
        while current != None:
            if current.get_title().lower() == title.lower() and previous != None:
                previous.set_next_track(current.get_next_track())
                # self.__len -= 1
                break
            if current.get_title().lower() == title.lower() and previous == None:
                self.__first_track = current.get_next_track()
                # self.__len -= 1
                break
            previous = current
            current = current.get_next_track()

    def length(self):
        # return self.__len
        current = self.__first_track
        count = 0
        while current != None:
            count += 1
            current = current.get_next_track()
        return count

    def print_tracks(self):
        current = self.__first_track
        count = 0
        while current != None:
            count += 1
            print(f"{count}. {current.get_title()}")
            current = current.get_next_track()
