lists_premise = 10
lists_hypothesis = 7

# the hypothesis refers to the number of top-10-movies lists, which is also mentioned in the premise
if lists_hypothesis <= lists_premise:
    # check if the hypothesis value contradicts the estimate of at least 'lists_premise' lists
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of lists
    # any number of lists greater than 'lists_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
