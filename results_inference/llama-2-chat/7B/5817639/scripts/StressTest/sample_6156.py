ages_ratio_premise = 5/4
ages_ratio_hypothesis = 3/4

# the hypothesis talks about the ratio of ages, which is also mentioned in the premise
if ages_ratio_hypothesis >= ages_ratio_premise:
    # check if the estimate of 'ages_ratio_hypothesis' contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of ages
    # any ratio greater than 'ages_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
