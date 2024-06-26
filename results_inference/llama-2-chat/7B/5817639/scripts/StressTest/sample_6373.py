pencils_premise = 425
pencils_hypothesis = 125

# the hypothesis talks about the number of pencils possessed by Shreehari, referenced also in the premise
if pencils_hypothesis <= pencils_premise:
    # check if the hypothesis value contradicts the estimate of less than 'pencils_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pencils
    # any number of pencils greater than 'pencils_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
