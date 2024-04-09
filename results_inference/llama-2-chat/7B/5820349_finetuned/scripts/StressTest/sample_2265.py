gloves_premise = 20
gloves_hypothesis = 60

# the hypothesis refers to the number of gloves Andy has, mentioned in the premise
if gloves_premise >= gloves_hypothesis:
    # check if the number of gloves in the premise contradicts the estimate of less than 'gloves_hypothesis'
    label = "contradiction"
else:
    # if the number of gloves in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
