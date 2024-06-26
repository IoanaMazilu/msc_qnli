drained_amount_premise = 5.12e9
drained_amount_hypothesis = 1e12

# the hypothesis and premise mention the amount drained out of the economy in July of 2017
if drained_amount_hypothesis!= drained_amount_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
