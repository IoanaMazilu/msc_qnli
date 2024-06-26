blue_paint_premise = 16
blue_paint_hypothesis = 36

# the hypothesis talks about the number of liters of blue paint needed to change Fuchsia to Mauve
if blue_paint_hypothesis <= blue_paint_premise:
    # check if the hypothesis value contradicts the estimate of more than 'blue_paint_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of liters of blue paint needed
    # any number of liters greater than 'blue_paint_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
