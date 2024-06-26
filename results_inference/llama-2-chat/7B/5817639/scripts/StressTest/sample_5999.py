top_movies_premise = 10
top_movies_hypothesis = 6

# the hypothesis talks about the number of top movies a film must appear in to be considered for movie of the year
if top_movies_hypothesis <= top_movies_premise:
    # check if the hypothesis value contradicts the estimate of at least 1/4 of the top movies in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of top movies
    # any number of top movies greater than 'top_movies_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
