floor_ Jose_premise = 51
floor_ Jose_hypothesis = 31
speed_ Jose_premise = 63
speed_ Jose_hypothesis = 63

# the hypothesis talks about Jose getting on an elevator on a different floor than the premise
if floor_ Jose_hypothesis!= floor_ Jose_premise:
    # check if the hypothesis floor is mentioned in the premise
    if floor_ Jose_premise in [floor_ Jose_hypothesis]:
        # if the hypothesis floor is mentioned in the premise, it's a contradiction
        label = "contradiction"
    else:
        # if the hypothesis floor is not mentioned in the premise, it's entailment
        label = "entailment"
else:
    # if the hypothesis floor is the same as the premise floor, it's neutral
    label = "neutral"

print(label)
