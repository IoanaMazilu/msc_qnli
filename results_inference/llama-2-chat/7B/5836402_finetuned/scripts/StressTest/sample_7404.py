lenses_premise = 2
lenses_hypothesis = 7

# the hypothesis refers to the number of lenses in each telescope, which is also mentioned in the premise
if lenses_hypothesis >= lenses_premise:
    # check if the estimate of 'lenses_hypothesis' contradicts the number of lenses in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
