lists_premise = 1/4
lists_hypothesis = 2/4

# the hypothesis refers to the number of top-10-movies lists needed for a film to be considered for the "movie of the year"
if lists_hypothesis >= lists_premise:
    # check if the hypothesis value contradicts the estimate of at least 'lists_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
