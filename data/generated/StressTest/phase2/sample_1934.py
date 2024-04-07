# Premise: Tom drives from town T to town B, driving at a constant speed of 60 miles per hour.
# Hypothesis: Tom drives from town T to town B, driving at a constant speed of 70 miles per hour.
# Golden Label: contradiction

speed_premise = 60
speed_hypothesis = 70

# the hypothesis refers to the speed Tom is driving, which is also mentioned in the premise
if speed_premise != speed_hypothesis:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the speeds are the same, we can infer entailment
    label = "entailment"

print(label)

