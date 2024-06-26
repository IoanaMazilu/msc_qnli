paint_premise = 2
paint_hypothesis = 1

# the hypothesis refers to the number of cans of paint mentioned in the premise
if paint_hypothesis >= paint_premise:
    # check if the hypothesis value contradicts the estimate of less than 'paint_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cans of paint
    # any number of cans of paint less than 'paint_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
