floor_premise = 51
floor_hypothesis = 61
rate_premise = 63
rate_hypothesis = 63

# the hypothesis refers to the floor Albert gets on and the rate he rides down, both mentioned in the premise
if floor_premise < floor_hypothesis:
    # check if the floor Albert gets on in the hypothesis contradicts the floor he gets on in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate Albert rides down in the hypothesis contradicts the rate he rides down in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
