floor_premise = 51
floor_hypothesis = 61
rate_premise = 63
rate_hypothesis = 63

# the hypothesis talks about the floor Albert gets on and the rate he rides down, both referenced in the premise
if floor_hypothesis <= floor_premise:
    # check if the hypothesis floor contradicts the premise floor
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the hypothesis rate contradicts the premise rate
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
