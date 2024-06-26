capital_belle_premise = 250
capital_belle_hypothesis = 350

# the hypothesis refers to the capital of Belle mentioned in the premise
if capital_belle_premise >= capital_belle_hypothesis:
    # check if the estimate of 'capital_belle_hypothesis' contradicts the value of Belle's capital in the premise
    label = "contradiction"
else:
    # if the capital value in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
