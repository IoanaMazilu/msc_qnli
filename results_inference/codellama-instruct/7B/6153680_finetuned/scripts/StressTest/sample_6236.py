speed_doubled_premise = "If Anne's speed were doubled"
speed_doubled_hypothesis = "If Anne's speed were doubled"

# the hypothesis and premise mention the same situation where Anne's speed is doubled
if speed_doubled_premise == speed_doubled_hypothesis:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis and premise do not contradict each other
    label = "neutral"

print(label)
