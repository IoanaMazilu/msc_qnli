seized_amount_premise = 2000000
seized_amount_hypothesis = 2000000

# the hypothesis mentions the seized amount of methamphetamine, which is also mentioned in the premise
if seized_amount_hypothesis!= seized_amount_premise:
    # check if the seized amount in the hypothesis contradicts the seized amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
