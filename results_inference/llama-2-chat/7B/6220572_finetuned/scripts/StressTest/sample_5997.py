top_10_movies_lists_premise = 1/4
top_10_movies_lists_hypothesis = 4/4

# the hypothesis refers to the number of top-10-movies lists in which a film must appear, as mentioned in the premise
if top_10_movies_lists_hypothesis <= top_10_movies_lists_premise:
    # check if the estimate of 'top_10_movies_lists_hypothesis' contradicts the fraction of top-10-movies lists in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the fraction of top-10-movies lists
    # any fraction greater than 'top_10_movies_lists_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
