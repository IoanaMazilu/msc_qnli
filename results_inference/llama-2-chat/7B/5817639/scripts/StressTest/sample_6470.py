carpet_premise = 20
carpet_hypothesis = 40

# the hypothesis talks about the percentage of the living room floor covered by a carpet
if carpet_hypothesis <= carpet_premise:
    # check if the hypothesis value contradicts the estimate of 'carpet_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of the living room floor covered by a carpet
    # any percentage greater than 'carpet_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
