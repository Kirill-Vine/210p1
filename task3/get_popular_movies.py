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
def get_popular_movies(f, n=10):
    dct=sorted(f.items(), key=lambda item: item[1], reverse=True)
    if len(dct)>n:
        while len(dct) != n:
            dct.pop()
    return dct
get_popular_movies(calculate_average_rating(read_ratings_data("movieRatingSample.txt")),11)
