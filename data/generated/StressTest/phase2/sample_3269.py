# Premise: At the same time Joyce gets on an elevator on the 41 st floor of the same building and rides down at a rate of 63 floors per minute.
# Hypothesis: At the same time Joyce gets on an elevator on the 71 st floor of the same building and rides down at a rate of 63 floors per minute.
# Golden Label: contradiction

floor_premise = 41
floor_hypothesis = 71
rate_premise = 63
rate_hypothesis = 63

# the hypothesis refers to the floor number and elevator speed mentioned in the premise
if floor_premise != floor_hypothesis:
    # check if the floor number in the hypothesis contradicts the floor number reported in the premise
    label = "contradiction"
elif rate_premise != rate_hypothesis:
    # check if the elevator speed in the hypothesis contradicts the elevator speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

