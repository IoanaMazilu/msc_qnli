lenses_premise = 2
lenses_hypothesis = 2

# the hypothesis refers to the number of lenses in a telescope mentioned in the premise
if lenses_hypothesis <= lenses_premise:
    # check if the hypothesis value contradicts the number of lenses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
