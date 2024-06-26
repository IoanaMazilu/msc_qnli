movie_length_premise = 100
movie_length_hypothesis = 100

# the hypothesis talks about the same movie length as the premise
if movie_length_hypothesis!= movie_length_premise:
    # check if the hypothesis value contradicts the estimate of'movie_length_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the movie length
    # any number of minutes greater than'movie_length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
