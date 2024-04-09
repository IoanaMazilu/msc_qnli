kentucky_derby_premise = 3
kentucky_derby_hypothesis = 4

# the hypothesis refers to the number of fastest horses to be submitted to the Kentucky Derby, while the premise refers to the same
if kentucky_derby_hypothesis <= kentucky_derby_premise:
    # check if the hypothesis value contradicts the estimate of 'kentucky_derby_premise'
    label = "contradiction"
else:
    # the premise only provides an estimate for the number of fastest horses,
    # any number of fastest horses greater than 'kentucky_derby_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
