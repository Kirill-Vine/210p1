def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # get list of movies in genre
    movies = genre_to_movies[genre]
    #print(movies)
    movies_to_rating_sort = sorted(movie_to_average_rating.keys(), key = lambda item: item[1], reverse=True)
    #print(type(movies_to_rating_sort))
    if len(movies) < n:
        #print(movies_to_rating_sort)
        return movies_to_rating_sort
    else:
        dct = {}
        for movie in movies:
            dct[movie] = movie_to_average_rating[movie]
        #print(dct)
        movies_to_rating_sort = sorted(dct.items(), key = lambda item: item[1], reverse = True)
        dctFinal = {}
        for movie in movies_to_rating_sort[0:n]:
            dctFinal[movie[0]] = movie_to_average_rating[movie[0]]
        #print(dctFinal)
        return dctFinal
