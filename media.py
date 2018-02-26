##########################################
# Project: Movie Website
# Date Started: 22/02/2018
# Date Completed: 26/02/2018
# Submitted by: Rodrigo Montebello Saboya Brito
##########################################

######################################## Media File ####################################################
# Description: This file creates the class Movie to allow for instances of this class to be used in the
#              entertainment.py file. This definition of the class Movie was obtained through the course
########################################################################################################

class Movies():
    """ Class that defines a movie. """

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

