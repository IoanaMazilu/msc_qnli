pencils_premise = 125
pencils_hypothesis = 525

# the hypothesis talks about the number of pencils owned by Shreehari, which is also mentioned in the premise
if pencils_hypothesis > pencils_premise:
    # check if the hypothesis value contradicts the estimate of 'pencils_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pencils
    # any number of pencils greater than 'pencils_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
