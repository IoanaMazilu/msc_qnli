total_ages_premise = 66
total_ages_hypothesis = 66

# the hypothesis talks about the total of the ages of 3 people, which is also mentioned in the premise
if total_ages_hypothesis == total_ages_premise:
    # the hypothesis value matches the premise value, so entailment
    label = "entailment"
elif total_ages_hypothesis < total_ages_premise:
    # the hypothesis value is less than the premise value, so contradiction
    label = "contradiction"
else:
    # if the hypothesis value is equal to the premise value, but cannot be explicitly entailed from the premise, so neutral
    label = "neutral"

print(label)
