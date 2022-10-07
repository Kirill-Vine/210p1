def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    genre_rating = {}
    dct = {}

    for genre in genre_to_movies:
        rating = []
        for movie in genre_to_movies[genre]:
            rating.append(movie_to_average_rating[movie])

        avg_rating = sum(rating)/len(rating)

        genre_rating[genre] = avg_rating

    genre_to_rating_sort = sorted(genre_rating.items(), key = lambda item: item[1], reverse = True)

    if len(genre_rating) < n:
        allGenre = [i[0] for i in genre_to_rating_sort]
        return allGenre
    else:
        for genre in genre_to_rating_sort[0:n]:
            dct[genre[0]] = genre_rating[genre[0]]
            #print(genre_to_rating_sort)

    return dct
    
    
    
    #return genre:average rating
