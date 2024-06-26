fishing_time_premise = 20
fishing_time_hypothesis = 40

# the hypothesis offers a different account of the fishing time, compared to the one in the premise
if fishing_time_hypothesis != fishing_time_premise:
    # check if the fishing time in the hypothesis contradicts the one mentioned in the premise
    label = "contradiction"
else:
    # the fishing times are identical, so the premise and the hypothesis are consistent
    label = "entailment"

print(label)
