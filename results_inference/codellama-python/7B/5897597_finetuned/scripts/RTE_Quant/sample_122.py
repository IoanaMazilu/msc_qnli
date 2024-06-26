costs_premise = 14.3e9
costs_hypothesis = 14.3e9

# the hypothesis talks about the costs of Parmalat, which is also mentioned in the premise
if costs_hypothesis!= costs_premise:
    # check if the costs in the hypothesis contradicts the costs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
