import webbrowser

class Movie():

    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.trailer_youtube_url = poster_image
        self.poster_image_url = trailer_youtube

    def ShowTrailer(self):
        webbrowser.open(self.poster_url)
