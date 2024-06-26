blue_paint_premise = 16
blue_paint_hypothesis = 36

# the hypothesis talks about the number of liters of blue paint to mix with Fuchsia to get Mauve, referenced also in the premise
if blue_paint_hypothesis!= blue_paint_premise:
    # check if the number of liters of blue paint in the hypothesis contradicts the number of liters of blue paint in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of liters of blue paint
    # any number of liters of blue paint consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
