settlement_amount_premise = 5.1e9 # billion is represented as e9
settlement_amount_hypothesis = 5.1e9

# the hypothesis and premise mention the settlement amount Goldman Sachs has to pay for the US mortgage investigation
if settlement_amount_premise != settlement_amount_hypothesis:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
