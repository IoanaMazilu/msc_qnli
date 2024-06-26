rainfall_premise = 25
rainfall_hypothesis = 25

# the hypothesis refers to the total rainfall in the first two weeks of March mentioned in the premise
if rainfall_hypothesis <= rainfall_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
