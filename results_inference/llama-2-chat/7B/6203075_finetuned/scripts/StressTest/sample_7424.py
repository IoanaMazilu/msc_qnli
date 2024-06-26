floor_premise = 51
floor_hypothesis = 81
rate_premise = 63
rate_hypothesis = 63

# the hypothesis talks about the floor Albert gets on and the rate he rides down, both referenced in the premise
if floor_hypothesis!= floor_premise:
    # check if the floor Albert gets on in the hypothesis contradicts the floor he gets on in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate Albert rides down in the hypothesis contradicts the rate he rides down in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
