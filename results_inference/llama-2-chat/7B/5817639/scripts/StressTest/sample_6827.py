ages_premise = 4
ages_hypothesis = 1

# the hypothesis talks about the ratio between the ages of two people, referenced also in the premise
if ages_hypothesis <= ages_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio, and the hypothesis value is consistent with it
    label = "entailment"

print(label)
