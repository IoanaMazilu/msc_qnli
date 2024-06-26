commute_difference_premise = 15
commute_difference_hypothesis = 15

# the hypothesis refers to the difference in commuting time by walking and by train, as mentioned in the premise
if commute_difference_hypothesis <= commute_difference_premise:
    # check if the hypothesis estimate contradicts the premise
    label = "contradiction"
else:
    # the premise gives an exact difference in commuting time
    # any difference greater than 'commute_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
