floor_premise = 11
floor_hypothesis = 81
rate_premise = 57
rate_hypothesis = 57

# the hypothesis talks about the floor David gets on and the rate he rides up, which are also mentioned in the premise
if floor_hypothesis!= floor_premise:
    # check if the floor in the hypothesis contradicts the floor in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
