damaged_premise = 1
threatened_premise = 5

# the premise mentions the number of buildings damaged and threatened by the fire, which is also referenced in the hypothesis
if damaged_hypothesis == damaged_premise:
    # check if the number of buildings damaged in the hypothesis matches the number in the premise
    label = "entailment"
elif threatened_hypothesis!= threatened_premise:
    # check if the number of buildings threatened in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
