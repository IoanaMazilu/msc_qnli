movie_of_year_premise = 4
movie_of_year_hypothesis = 1

# the hypothesis talks about the number of top-10 movies lists a film must appear in to be considered for movie of the year
if movie_of_year_hypothesis <= movie_of_year_premise:
    # check if the hypothesis value contradicts the estimate of at least'movie_of_year_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of top-10 movies lists
    # any number of top-10 movies lists a film must appear in to be considered for movie of the year is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
