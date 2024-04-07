# Premise: Tom drives from town R to town B, driving at a constant speed of 60 miles per hour.
# Hypothesis: Tom drives from town R to town B, driving at a constant speed of more than 50 miles per hour.
# Golden Label: entailment

speed_premise = 60
speed_hypothesis = 50

# the hypothesis refers to the speed at which Tom drives, which is also mentioned in the premise
if speed_premise < speed_hypothesis:
    # check if the speed in the premise contradicts the hypothesis speed
    label = "contradiction"
elif speed_premise > speed_hypothesis:
    # if the speed in the premise is greater than the speed in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the speeds are equal, the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

