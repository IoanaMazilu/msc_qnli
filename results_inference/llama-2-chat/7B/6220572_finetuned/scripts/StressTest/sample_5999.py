movie_year_premise = 1/4
movie_year_hypothesis = 6/4

# the hypothesis refers to the fraction of top-10-movies lists in which a film must appear to be considered for "movie of the year"
if movie_year_hypothesis == movie_year_premise:
    # check if the hypothesis value contradicts the fraction of lists in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the fraction of lists
    # any fraction greater than'movie_year_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
