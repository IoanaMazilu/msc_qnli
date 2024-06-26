pencils_premise = 425
pencils_hypothesis = 125

# the hypothesis refers to the number of pencils owned by Shreehari
if pencils_hypothesis <= pencils_premise:
    # check if the hypothesis value contradicts the estimate of 'pencils_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pencils
    # any number of pencils less than or equal to 125 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
