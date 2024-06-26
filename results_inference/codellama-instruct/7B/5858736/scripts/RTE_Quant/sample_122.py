premise_cost = 14.3e9
hypothesis_cost = 14.3e9

# the hypothesis talks about the cost of Parmalat, which is also mentioned in the premise
if hypothesis_cost!= premise_cost:
    # check if the cost in the hypothesis contradicts the cost in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
