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
def calculate_average_rating(dct):
    result = {}
    for(name,ratingList) in dct.items():
        sum = 0
        count = 0
        for rating in ratingList:
            sum += float(rating)
            count += 1
        avrg = float("{:.1f}".format(sum/count))
        result[name] = avrg
    return result
calculate_average_rating(read_ratings_data("movieRatingSample.txt"))
