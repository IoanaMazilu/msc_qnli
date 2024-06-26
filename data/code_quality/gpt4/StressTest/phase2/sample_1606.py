death_rate_premise = 2
death_rate_hypothesis = 5
flee_rate = 15  # same for both premise and hypothesis

# the hypothesis talks about the death and flee rates in a village, referenced also in the premise
if death_rate_hypothesis <= death_rate_premise:
    # check if the death rate in the hypothesis contradicts the estimate of more than 'death_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the death rate
    # any death rate greater than 'death_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
