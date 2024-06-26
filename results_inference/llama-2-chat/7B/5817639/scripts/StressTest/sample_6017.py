years_premise = 20
years_hypothesis = 40

# the hypothesis refers to the age at which Jane started baby-sitting, which is not mentioned in the premise
if years_hypothesis <= years_premise:
    # check if the estimate of 'years_hypothesis' contradicts the age mentioned in the premise
    label = "contradiction"
else:
    # the premise does not provide any information about the age at which Jane started baby-sitting, so we cannot infer entailment or contradiction
    label = "neutral"

print(label)
