lenses_premise = 2
lenses_hypothesis = 7

# the hypothesis refers to the number of lenses in each telescope, mentioned in the premise
if lenses_premise >= lenses_hypothesis:
    # check if the estimate of 'lenses_hypothesis' contradicts the number of lenses in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
