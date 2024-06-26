floor_premise = 51
floor_hypothesis = 81
rate_premise = 63
rate_hypothesis = 63

# the hypothesis talks about Albert's floor and rate of descent, which are also mentioned in the premise
if floor_hypothesis!= floor_premise:
    # check if the floor number in the hypothesis contradicts the floor number in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate of descent in the hypothesis contradicts the rate of descent in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
