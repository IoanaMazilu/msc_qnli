days_walked_premise = 3
days_walked_hypothesis = 3

# the hypothesis and the premise refer to the same number of days walked
if days_walked_hypothesis <= days_walked_premise:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise
    label = "neutral"

print(label)
