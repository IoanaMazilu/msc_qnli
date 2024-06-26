rosy_efficiency_premise = 10
rosy_efficiency_hypothesis = 30

# the hypothesis refers to Rosy's efficiency compared to Mary, mentioned in the premise
if rosy_efficiency_hypothesis <= rosy_efficiency_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, we can infer entailment
    label = "entailment"

print(label)
