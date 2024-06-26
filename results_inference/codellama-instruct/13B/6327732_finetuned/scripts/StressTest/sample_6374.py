pencils_premise = 125
pencils_hypothesis = 525

# the hypothesis refers to the number of pencils mentioned in the premise
if pencils_hypothesis <= pencils_premise:
    # check if the estimate of 'pencils_hypothesis' contradicts the number of pencils in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of pencils
    # any number of pencils greater than 'pencils_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
