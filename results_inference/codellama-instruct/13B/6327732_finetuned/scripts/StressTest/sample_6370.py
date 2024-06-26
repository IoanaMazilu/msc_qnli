cans_paint_premise = 8
cans_paint_hypothesis = 4

# the hypothesis refers to the number of cans of paint mentioned in the premise
if cans_paint_hypothesis <= cans_paint_premise:
    # check if the estimate of 'cans_paint_hypothesis' contradicts the number of cans of paint in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cans of paint
    # any number of cans of paint greater than 'cans_paint_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
