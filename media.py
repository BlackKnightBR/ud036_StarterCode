class Movies():
    """ Class that defines a movie. """

    # Function that intanciates the class Movies,
    # using as parameter, title, art(poster)
    # and url youtube trailer

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """
            Inicializes intances of Movies class,
            :param movie_title: string
            :param poster_image: string
            :param trailer_youtube: string
        """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

