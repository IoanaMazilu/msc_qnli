average_increase_premise = 2
average_increase_hypothesis = 7

# the hypothesis refers to Jerry's desire to raise his average mentioned in the premise
if average_increase_hypothesis <= average_increase_premise:
    # check if the hypothesis estimate contradicts the premise average increase
    label = "contradiction"
elif average_increase_hypothesis > average_increase_premise:
    # any average increase greater than 'average_increase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
