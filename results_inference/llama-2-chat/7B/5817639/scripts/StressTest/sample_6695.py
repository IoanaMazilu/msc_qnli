after_premise = 14000
after_hypothesis = float("less than 14000")

# the hypothesis talks about the amount of money John withdraws after 8 months, referenced also in the premise
if after_hypothesis <= after_premise:
    # check if the hypothesis value contradicts the estimate of 'after_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money John withdraws
    # any amount of money less than 'after_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
