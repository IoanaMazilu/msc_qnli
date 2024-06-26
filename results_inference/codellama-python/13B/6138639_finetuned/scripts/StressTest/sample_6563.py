average_increase_premise = 2
average_increase_hypothesis = 2

# the hypothesis refers to the increase in average Jerry wants, which is also mentioned in the premise
if average_increase_hypothesis <= average_increase_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact increase in average
    # any increase greater than 'average_increase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
