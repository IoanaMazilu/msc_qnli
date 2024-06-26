floor_premise = 41
floor_hypothesis = 11
rate_premise = 63
rate_hypothesis = 63

# the hypothesis refers to the same situation described in the premise
if floor_premise <= floor_hypothesis:
    # check if the premise floor contradicts the hypothesis floor
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate of floors per minute in the hypothesis contradicts the rate of floors per minute reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
