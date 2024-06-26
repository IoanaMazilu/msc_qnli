# Building floor levels in the premise and hypothesis
floor_premise = 51
floor_hypothesis = 31
rate_premise = 63
rate_hypothesis = 63

# The hypothesis refers to the same building and the same elevator ride as the premise
if floor_hypothesis!= floor_premise:
    # Check if the floor level in the hypothesis contradicts the floor level in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # Check if the rate of elevator ride in the hypothesis contradicts the rate of elevator ride in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
