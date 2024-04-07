# Premise: Paul can dig the same well in 24 days.
# Hypothesis: Paul can dig the same well in less than 24 days.
# Golden Label: contradiction

digging_time_premise = 24
digging_time_hypothesis = 24

# the hypothesis refers to the time Paul needs to dig the well, mentioned also in the premise
if digging_time_hypothesis < digging_time_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif digging_time_hypothesis == digging_time_premise:
    # check if the hypothesis value is exactly the same as the premise
    label = "entailment"
else:
    # the premise gives the exact time for digging the well
    # any time greater than 'digging_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

