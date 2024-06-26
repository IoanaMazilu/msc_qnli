floor_premise = 51
floor_hypothesis = 31
rate_premise = 63
rate_hypothesis = 63

# the hypothesis talks about the floor Jose gets on and the rate at which he rides down, both referenced in the premise
if floor_hypothesis!= floor_premise:
    # check if the floor in the hypothesis contradicts the floor mentioned in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
