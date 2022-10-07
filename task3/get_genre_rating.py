def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    genre_to_movies = genre_to_movies
    movie_to_average_rating = movie_to_average_rating
    genre_rating = {}
    rating = []
    dct = {}
    
    for movie in genre_to_movies[genre]:
        rating.append(movie_to_average_rating[movie])
        
    avg_rating = sum(rating)/len(rating)
        
    dct[genre] = avg_rating
    
    return dct
