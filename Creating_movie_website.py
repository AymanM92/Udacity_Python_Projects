import Movie_Class
import fresh_tomatoes

toystory = Movie_Class.Movie("Toy Story","Toy Story","https://www.youtube.com/watch?v=KYz2wyBy3kc","https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg")
avatar = Movie_Class.Movie("Avatar","Avatar","https://www.youtube.com/watch?v=5PSNL1qE6VY","https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg")

Movie_list= [toystory,avatar]

fresh_tomatoes.open_movies_page(Movie_list)