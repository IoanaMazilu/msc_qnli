movie_of_year_premise = 1/4
movie_of_year_hypothesis = less_than_2/4

# the hypothesis talks about the percentage of top-10 movies lists that a film must appear in to be considered for movie of the year
if movie_of_year_hypothesis <= movie_of_year_premise:
    # check if the hypothesis value contradicts the estimate of at least 1/4 in the premise
    label = "contradiction"
else:
    # the premise gives an estimate of at least 1/4, which is consistent with the hypothesis but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
