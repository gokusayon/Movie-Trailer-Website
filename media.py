import webbrowser


class Movie():
	""" This class stores inforation about the movie !!

	Args:
		movie_title (str) : Name of the movie.
		movie_storyline (str) : Movie Synopsis.
		poster_image (str) : Image url for the poster of the movie.
		trailer_youtube (str) : Youtube url for the movie trailer.

	"""
    def __init__(self, movie_title, movie_storyline, 
    	poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
    	"""This function is used to show tailer in new window"""
        webbrowser.open(self.trailer_youtube_url)
