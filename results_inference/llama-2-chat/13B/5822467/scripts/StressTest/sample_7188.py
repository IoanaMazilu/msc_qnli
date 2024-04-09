train_leaves_jammu_premise = 12
train_leaves_jammu_hypothesis = 42

# the hypothesis talks about the time of departure, which is a numerical value
if train_leaves_jammu_hypothesis < train_leaves_jammu_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif train_leaves_jammu_hypothesis == train_leaves_jammu_premise:
    # check if the hypothesis value is consistent with the premise value
    label = "entailment"
else:
    # the premise gives a specific value for the time of departure
    # any time of departure before 12 noon is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
