ages_premise = 45
ages_hypothesis = 35

# the hypothesis talks about the total of the ages of three people, referenced also in the premise
if ages_hypothesis <= ages_premise:
    # check if the hypothesis value contradicts the estimate of the total age in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the total age, and any total age greater than 'ages_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
