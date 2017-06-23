import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story about Toys !",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A story about a marine on other planet !",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

wonder_woman = media.Movie("Wonder woman", "A story about a amazonian goddess on a quest to save the planet !",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                           "https://www.youtube.com/watch?v=1Q8fG0TtVAY")

logan = media.Movie("Logan", "A story about a marine on other planet",
                    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

spiderman_homecoming = media.Movie("Spider-Man: Homecoming", "Spiderman is back and this time in MCU !",
                                   "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
                                   "https://www.youtube.com/watch?v=xrzXIaTt99U")

mummy = media.Movie("The Mummy", "A betrayed Egyption Princess, a honest to god (?) soldier ,what can possibly go wrong ?",
                    "https://upload.wikimedia.org/wikipedia/en/a/a2/The_Mummy_%282017%29.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")


movies = [toy_story, avatar, wonder_woman,
          logan, spiderman_homecoming, mummy]

fresh_tomatoes.open_movies_page(movies)
