efficiency_premise = 10
efficiency_hypothesis = 10

# the hypothesis refers to the efficiency difference between Rosy and Mary mentioned in the premise
if efficiency_hypothesis >= efficiency_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise one, we can infer entailment
    label = "entailment"

print(label)
