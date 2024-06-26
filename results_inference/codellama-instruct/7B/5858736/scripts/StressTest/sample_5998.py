premise_min_lists = 4/4
hypothesis_min_lists = 1/4

# the hypothesis refers to the minimum number of lists a film must appear in to be considered for "movie of the year"
if hypothesis_min_lists <= premise_min_lists:
    # check if the hypothesis value contradicts the estimate of at least 'premise_min_lists'
    label = "contradiction"
else:
    # the premise gives only an estimate for the minimum number of lists
    # any number of lists greater than 'premise_min_lists' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
