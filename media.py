import webbrowser

"""This class provides a way to store movie related information"""
# This class provides a way to store movie related information
# title, story line, reviews, poster, trailer link
# _ _ two underscore is used to tell that init is python keyword
# it is already reclared
# self is pointing to that object only for eg if toystory object is created
# then self mean toystory


class Movie():

    def __init__(self,
                 movie_title,
                 movie_rating,
                 poster_image,
                 trailer_youtube):
        # initialize instance of class Movie
        self.title = movie_title
        self.rate = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
