floor_premise = 51
floor_hypothesis = 71
rate_premise = 93
rate_hypothesis = 93

# the hypothesis talks about the floor Joyce gets on and the rate of descent, which are also mentioned in the premise
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
