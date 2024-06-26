lenses_premise = 2
lenses_hypothesis = 7

# the hypothesis refers to the number of lenses in each telescope, which is also mentioned in the premise
if lenses_hypothesis <= lenses_premise:
    # check if the hypothesis value contradicts the number of lenses in the premise
    label = "entailment"
else:
    # if the hypothesis value is greater than the premise value, it contradicts the premise
    label = "contradiction"

print(label)
