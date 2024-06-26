gloves_premise = 20
gloves_hypothesis = 60

# the hypothesis refers to the number of pairs of gloves mentioned in the premise
if gloves_premise < gloves_hypothesis:
    # check if the estimate of 'gloves_hypothesis' contradicts the number of gloves in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
