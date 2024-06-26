deal_amount_premise = 3000000000
deal_amount_hypothesis = 3000000000

# the hypothesis mentions the amount of the deal, which is also mentioned in the premise
if deal_amount_hypothesis!= deal_amount_premise:
    # check if the deal amount in the hypothesis contradicts the deal amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
