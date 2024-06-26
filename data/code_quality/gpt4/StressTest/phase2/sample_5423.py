capital_premise = 120
capital_hypothesis = 120

# the hypothesis refers to the same capital amount mentioned in the premise
if capital_hypothesis < capital_premise:
    # check if the hypothesis value contradicts the exact value of 'capital_premise'
    label = "contradiction"
elif capital_hypothesis > capital_premise:
    # check if the hypothesis value contradicts the exact value of 'capital_premise' 
    label = "contradiction"
else:
    # if the hypothesis value is the same as the premise value, we can infer entailment
    label = "entailment"

print(label)
