blue_paint_hypothesis = 16
blue_paint_premise = 86

# the hypothesis talks about the number of liters of blue paint needed to change Fuchsia paint
# the premise gives an estimate for the number of liters of Fuchsia paint
if blue_paint_hypothesis <= blue_paint_premise:
    # check if the hypothesis value contradicts the estimate of more than 'blue_paint_premise' liters of blue paint
    label = "contradiction"
else:
    # any number of liters of blue paint less than 'blue_paint_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
