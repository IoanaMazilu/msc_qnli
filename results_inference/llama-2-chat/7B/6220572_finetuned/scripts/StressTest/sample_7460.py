top_movies_lists_premise = 1/4
top_movies_lists_hypothesis = 3/4

# the hypothesis refers to the percentage of top-10-movies lists that a film must appear in, also mentioned in the premise
if top_movies_lists_hypothesis <= top_movies_lists_premise:
    # check if the hypothesis value contradicts the estimate of 'top_movies_lists_premise'
    label = "contradiction"
else:
    # any percentage greater than 'top_movies_lists_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
