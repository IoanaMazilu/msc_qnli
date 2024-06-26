paint_cans_premise = 4
paint_cans_hypothesis = 8

# the hypothesis refers to the number of paint cans mentioned in the premise
if paint_cans_hypothesis <= paint_cans_premise:
    # check if the hypothesis value contradicts the estimate of 'paint_cans_premise'
    label = "contradiction"
elif paint_cans_hypothesis > paint_cans_premise:
    # if the hypothesis value is greater than the premise, it can be entailed
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise, it cannot be entailed
    label = "neutral"

print(label)
