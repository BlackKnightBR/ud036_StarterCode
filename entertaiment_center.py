import media
import fresh_tomatoes


# Instances of the class Movies, imported from the file media
into_the_wild = media.Movies(
    "Into The Wild",
    "https://resizing.flixster.com/QVAYl1_7N8StUG8JkUo28qdjxDY=/206x305/" +
    "v1.bTsxMTYyMjIxNztqOzE3Njg0OzEyMDA7NzkyOzEwNTY",
    "https://www.youtube.com/watch?v=g7ArZ7VD-QQ"
)

toy_story = media.Movies(
    "Toy Story",
    "https://img.fstatic.com/p3ICCo1m3Vo2YVgG1ownzV0f-38=/fit-in/290x478/" +
    "smart/https://cdn.fstatic.com/media/movies/covers/2014/06/" +
    "toy-story_t1407.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc&t=5s"
)

transformers = media.Movies(
    "Transformers",
    "http://www.firstshowing.net/img/optimus-poster-big.jpg?x10994",
    "https://www.youtube.com/watch?v=HKi0xnV4ZjM"
)

the_wrestler = media.Movies(
    "The Wrestler",
    "https://img.fstatic.com/LUPN-Twzy1S6-mHI4o8GmWrWfsM=/fit-in/" +
    "290x478/smart/https://cdn.fstatic.com/media/movies/covers/2012/05/" +
    "99246ed694dab1d32c896bac1b4bf785.jpg",
    "https://www.youtube.com/watch?v=61-GFxjTyV0"
)

batman = media.Movies(
    "Batman The Dark Knight Rises",
    "https://vignette.wikia.nocookie.net/marvel_dc/images/0/05/" +
    "The_Dark_Knight_Rises_poster.jpg/revision/latest/scale-to-width" +
    "-down/324?cb=20120123215909",
    "https://www.youtube.com/watch?v=g8evyE9TuYk"
)

x_machina = media.Movies(
    "X Machina",
    "http://www.joblo.com/timthumb.php?src=/posters/images/full/" +
    "ex-machina-large.jpg&h=273&w=183&q=100",
    "https://www.youtube.com/watch?v=PI8XBKb6DQk"
)

george_harrison = media.Movies(
    "George Harrison into the material world",
    "https://www.superseventies.com/oaaa/oaaa_harrison2_thumb.jpg",
    "https://www.youtube.com/watch?v=fJh9O8pI4Ck"
)

born_strong = media.Movies(
    "Born Strong",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNm" +
    "ViNzk2ZGYtN2Q4My00MzU4LWFhOTctZDE2Zjc0OWY1NmI5XkEyXkFqcGde" +
    "QXVyMTI0Nzg3MTM@._V1_UY268_CR1,0,182,268_AL_.jpg",
    "https://www.youtube.com/watch?v=dhS7hut7xoE"
)

easy_rider = media.Movies(
    "Easy Rider",
    "https://www.movieposter.com/posters/archive/main/47/MPW-23917",
    "https://www.youtube.com/watch?v=GwST6mpT7Ds"
)

# Creates a list with all the movies available in this file
movies = [
    into_the_wild, toy_story,
    transformers,
    the_wrestler,
    batman,
    x_machina,
    george_harrison,
    born_strong,
    easy_rider
]

# Call's the function wich opens the page(html)
# Using the list above as parameter
fresh_tomatoes.open_movies_page(movies)

