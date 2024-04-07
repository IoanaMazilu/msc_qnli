# Premise: Tom drives from town E to town B, driving at a constant speed of 60 miles per hour.
# Hypothesis: Tom drives from town E to town B, driving at a constant speed of more than 60 miles per hour.
# Golden Label: contradiction

speed_premise = 60
speed_hypothesis = 60

# the hypothesis talks about the speed at which Tom drives, which is also mentioned in the premise
if speed_hypothesis > speed_premise:
    # check if the hypothesis speed contradicts the speed stated in the premise
    label = "contradiction"
elif speed_hypothesis == speed_premise:
    # if the speed in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"
else:
    # any speed lower than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

