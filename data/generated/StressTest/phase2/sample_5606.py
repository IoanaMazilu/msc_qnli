# Premise: While driving from City A to City B, Glen drives at a constant speed of 40 miles per hour.
# Hypothesis: While driving from City A to City B, Glen drives at a constant speed of 50 miles per hour.
# Golden Label: contradiction

speed_premise = 40
speed_hypothesis = 50

# the hypothesis refers to the speed at which Glen drives from City A to City B, mentioned also in the premise
if speed_hypothesis == speed_premise:
    # check if the speed in the hypothesis is the same as the speed in the premise
    label = "entailment"
else:
    # if the speed in the hypothesis is not the same as the speed in the premise, it contradicts the premise
    label = "contradiction"

print(label)
