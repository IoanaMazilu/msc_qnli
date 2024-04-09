average_raise_premise = 2
average_raise_hypothesis = 2

# the hypothesis refers to the points Jerry wants to raise his average by, which is also mentioned in the premise
if average_raise_hypothesis <= average_raise_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact number for the points Jerry wants to raise his average by
    # any number of points greater than 'average_raise_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
