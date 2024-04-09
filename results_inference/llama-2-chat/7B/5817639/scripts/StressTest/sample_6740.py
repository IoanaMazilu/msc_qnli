paint_premise = 1
paint_hypothesis = 0

# the hypothesis refers to the amount of paint mentioned in the premise
if paint_hypothesis <= paint_premise:
    # check if the hypothesis value contradicts the estimate of 'paint_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of paint
    # any amount of paint less than 'paint_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
