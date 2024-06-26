lenses_premise = 2
lenses_hypothesis = 8

# the hypothesis refers to the number of lenses in each telescope, which is also mentioned in the premise
if lenses_hypothesis!= lenses_premise:
    # check if the number of lenses in the hypothesis contradicts the number of lenses in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
