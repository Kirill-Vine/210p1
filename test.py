import math
from collections import defaultdict
from collections import Counter

# You may not add any other imports

# For each function, replace "pass" with your code

# --- TASK 1: READING DATA ---

# 1.1
def read_ratings_data(f):
    dct = {}
    prevmovie=''
    for line in open(f):
        if prevmovie!=line[:line.index('|')]:
            rating=[]
        movie = line[:line.index('|')]
        rating.append(line[line.index('|')+1:line.index('|')+4])
        dct[movie]=rating
        prevmovie=movie
    return dct

# 1.2
def read_movie_genre(f):
    dct = {}
    prevmovie=''
    for line in open(f):
        if prevmovie!=line[line.index('|')+3:].strip('\n'):
            movie = line[line.index('|')+3:].strip('\n|')
            genre = line[:line.index('|')]
        dct[movie] = genre
        prevmovie=movie
    return dct

# --- TASK 2: PROCESSING DATA ---

# 2.1
def create_genre_dict(d):
    result= {}
    for(movie, genre) in d.items():
        if genre in result.keys():
            result[genre].append(movie)
        else:
            result[genre] = [movie]
    return result



# 2.2
def calculate_average_rating(d):
    result = {}
    for(name,ratingList) in d.items():
        sum = 0
        count = 0
        for rating in ratingList:
            sum += float(rating)
            count += 1
        avrg = float("{:.1f}".format(sum/count))
        result[name] = avrg
    return result

# --- TASK 3: RECOMMENDATION ---

# 3.1
def get_popular_movies(d, n=10):
    dct=sorted(d.items(), key=lambda item: item[1], reverse=True)
    if len(dct)>n:
        while len(dct) != n:
            dct.pop()
    return dct

# 3.2
def filter_movies(d, thres_rating=3):
    new_movie_rating = {}
    for (key,value) in d.items():
        if value >= thres_rating:
            new_movie_rating[key] = value

    return new_movie_rating


# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    movies = genre_to_movies[genre]
    movies_to_rating_sort = sorted(movie_to_average_rating.items(), key = lambda item: item[1], reverse=True)
    if len(movies) < n:
        allMovies = [i[0] for i in movies_to_rating_sort]
        return allMovies
    else:
        dct = {}
        for movie in movies:
            dct[movie] = movie_to_average_rating[movie]
        dctFinal = {}
        for movie in movies_to_rating_sort[0:n]:
            dctFinal[movie[0]] = movie_to_average_rating[movie[0]]
        return dctFinal

# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):

    genre_rating = {}
    rating = []
    dct = {}

    for movie in genre_to_movies[genre]:
        rating.append(movie_to_average_rating[movie])

    avg_rating = sum(rating)/len(rating)

    dct[genre] = avg_rating

    return dct

# 3.5
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
    
# --- TASK 4: USER FOCUSED ---

# 4.1
def read_user_ratings(f):
    dct = {}
    for line in open(f):
        if line[line.index('|')+5:].strip('\n') not in dct:
            dct[line[line.index('|')+5:].strip('\n')] = list()
        dct[line[line.index('|')+5:].strip('\n')].append(tuple((line[:line.index('|')],line[line.index('|')+1:line.index('|')+4])))
    return dct

# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    dct = user_to_movies.get(str(user_id))
    lst=list()
    movie=None
    for i in dct:
        lst.append(i[1])
    for i in dct:
        if i[1]==max(lst):
            movie=i[0]
    genre=movie_to_genre.get(str(movie))
    return genre

# 4.3
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    pass

# --- main function for your testing ---
def main():
    print(
        read_ratings_data("movieRatingSample.txt") , '\n',
        read_movie_genre('genreMovieSample.txt'),'\n',
        create_genre_dict(read_movie_genre('genreMovieSample.txt')),'\n',
        calculate_average_rating(read_ratings_data("movieRatingSample.txt")),'\n',
        get_popular_movies(calculate_average_rating(read_ratings_data("movieRatingSample.txt")),11),'\n',
        filter_movies(calculate_average_rating(read_ratings_data("movieRatingSample.txt")), thres_rating=3),'\n',
##        test this case for each genre and big/small n
        get_popular_in_genre(
            'Comedy',
            create_genre_dict(read_movie_genre('genreMovieSample.txt')),
            calculate_average_rating(read_ratings_data("movieRatingSample.txt")),
            n=5
            ),'\n',
##        test each genre
        get_genre_rating(
            'Comedy',
            create_genre_dict(read_movie_genre('genreMovieSample.txt')),
            calculate_average_rating(read_ratings_data("movieRatingSample.txt"))
            ),'\n',
        read_user_ratings("movieRatingSample.txt"),'\n',
        get_user_genre(43,read_user_ratings("movieRatingSample.txt"), read_movie_genre('genreMovieSample.txt')), '\n',
        genre_popularity(create_genre_dict(read_movie_genre('genreMovieSample.txt')), calculate_average_rating(read_ratings_data("movieRatingSample.txt")), n=5)

        )
   
main()
