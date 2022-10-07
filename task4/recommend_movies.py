def read_movie_genre(f): #1.2
    dct = {}
    prevmovie=''
    for line in open(f):
        if prevmovie!=line[line.index('|')+3:].strip('\n'):
            movie = line[line.index('|')+3:].strip('\n|')
            genre = line[:line.index('|')]
        dct[movie] = genre
        prevmovie=movie
    return dct
def read_user_ratings(f): #4.1
    dct = {}
    for line in open(f):
        if line[line.index('|')+5:].strip('\n') not in dct:
            dct[line[line.index('|')+5:].strip('\n')] = list()
        dct[line[line.index('|')+5:].strip('\n')].append(tuple((line[:line.index('|')],line[line.index('|')+1:line.index('|')+4])))
    return dct
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
def get_user_genre(uid,f,e):
    dct = f.get(str(uid))
    lst=list()
    movie=None
    for i in dct:
        lst.append(i[1])
    for i in dct:
        if i[1]==max(lst):
            movie=i[0]
    genre=e.get(str(movie))
    return genre
def recommend_movies(uid,f,e,g):
    utg=get_user_genre(uid,f,e) #user top genre
    movies=list()
    lst=list()
    for i in f.get(str(uid)):
        lst.append(i[0])
    for i in e.items():
        if i[1]==utg and i[0] not in lst:
            movies.append(i[0])
    dct={}
    for i in g.items():
        if i[0] in movies:
            dct[i[0]]=i[1]
    sorted(dct.items(), key=lambda item: item[1], reverse=True)
    return dct
recommend_movies(43,read_user_ratings("movieRatingSample.txt"), read_movie_genre('genreMovieSample.txt'), calculate_average_rating(read_ratings_data("movieRatingSample.txt")))
