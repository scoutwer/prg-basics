class Song:
    def __init__(self,Performer,Title,Album,Year):
        self.performer = Performer
        self.title = Title
        self.album = Album 
        self.year = Year 
    def __str__(self):
        return f"Performer: {self.performer}\bTitle:{self.title}\bAlbum: {self.album}\bYear: {self.year} "

# object creation
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)


## object usage
print(song1)
