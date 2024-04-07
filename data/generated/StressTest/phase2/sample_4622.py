# Premise: Altogether, Steve is spending 6 hours a day on the roads.
# Hypothesis: Altogether, Steve is spending 8 hours a day on the roads.
# Golden Label: contradiction

road_time_premise = 6
road_time_hypothesis = 8

# the hypothesis talks about the amount of time Steve spends on roads which is also mentioned in the premise
if road_time_hypothesis == road_time_premise:
    # check if the hypothesis value matches the premise value
    label = "entailment"
else:
    # if the hypothesis value and premise value do not match, there is a contradiction
    label = "contradiction"

print(label)

