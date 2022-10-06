def filter_movies(d, thres_rating=3):
    new_movie_rating = {}
    for (key,value) in d.items():
        if value >= thres_rating:
            new_movie_rating[key] = value
            
    return new_movie_rating
