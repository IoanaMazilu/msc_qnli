cost_premise = 14.3e9
cost_hypothesis = 14.3e9

# the hypothesis talks about the cost of Parmalat, which is also mentioned in the premise
if cost_hypothesis!= cost_premise:
    # check if the cost in the hypothesis contradicts the cost from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
