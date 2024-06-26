ages_premise = 3
ages_hypothesis = 5

# the hypothesis talks about the ratio of the ages of two people, referenced also in the premise
if ages_hypothesis <= ages_premise:
    # check if the hypothesis value contradicts the estimate of the ratio of ages in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio of ages, and the hypothesis value is consistent with it
    label = "entailment"

print(label)
