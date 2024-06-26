tip_percentage_john_premise = 15
tip_percentage_john_hypothesis = 85

# the hypothesis refers to the tip paid by John and Jane, mentioned in the premise
if tip_percentage_john_hypothesis < tip_percentage_john_premise:
    # check if the hypothesis value contradicts the percentage of the tip paid by John in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
