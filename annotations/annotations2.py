import datetime
import random
from typing import List


class Track:
    def __init__(self, title: str, duration: datetime.time) -> None:
        self.title = title
        self.duration = duration

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class Album:
    def __init__(self, title: str, artist: str, release_year: str, tracks: List[Track]) -> None:
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.tracks = tracks

    def all_tracks_shorter_than(self, minutes=0, seconds=0) -> List[Track]:
        duration = datetime.time(minute=minutes, second=seconds)
        return [track for track in self.tracks if track.duration < duration]


track_list = [Track(title=random.choice(['first', 'second', 'third', 'forth']) + str(random.randint(0, 1000)),
                    duration=datetime.time(minute=random.randint(3, 6), second=random.randrange(59))) for _ in
              range(14)]

album1 = Album(title='Another brick in the wall', artist='Pink Floyd', release_year='1970', tracks=track_list)

for t in album1.all_tracks_shorter_than(minutes=5, seconds=0):
    print(f'Track Title: {t.title} - Duration: {t.duration}')
