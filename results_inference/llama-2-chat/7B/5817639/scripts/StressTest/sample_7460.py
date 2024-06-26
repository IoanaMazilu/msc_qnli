top_movies_premise = 10
top_movies_hypothesis = 77

# the hypothesis talks about the number of top-10 movies a film must appear in to be considered for movie of the year
if top_movies_hypothesis <= top_movies_premise:
    # check if the hypothesis value contradicts the estimate of at least 'top_movies_premise' top-10 movies
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of top-10 movies
    # any number of top-10 movies greater than 'top_movies_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
