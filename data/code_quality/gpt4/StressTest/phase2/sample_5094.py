average_increase_premise = 3
average_increase_hypothesis = 5

# the hypothesis refers to the amount Jerry wants to raise his average by, which is also mentioned in the premise
if average_increase_premise >= average_increase_hypothesis:
    # check if the 'average_increase_hypothesis' contradicts the premise
    label = "contradiction"
elif average_increase_hypothesis > average_increase_premise:
    # the premise gives a specific value for the average increase
    # a higher average increase is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
