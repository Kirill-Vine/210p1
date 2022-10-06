def calculate_average_rating(d):
    ans = {}
    for(name,ratingList) in d.items():
        sum = 0
        count = 0
        for rating in ratingList:
            sum+=float(rating)
            count+=1
        average = float("{:.1f}".format(sum/count))
        ans[name] = average
    return ans

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

def filter_movies(d, thres_rating=3):
    new_movie_rating = {}
    for (key,value) in d.items():
        if value >= thres_rating:
            new_movie_rating[key] = value
            
    return new_movie_rating

filter_movies(calculate_average_rating(read_ratings_data("movieRatingSample.txt")), thres_rating=3)
