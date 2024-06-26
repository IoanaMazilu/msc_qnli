charge_per_transaction_premise = 0.75 / 3
charge_per_transaction_hypothesis = 0.75 / 2

# The hypothesis refers to the charge per transaction mentioned in the premise
if charge_per_transaction_hypothesis > charge_per_transaction_premise:
    # Check if the charge per transaction in the hypothesis contradicts the charge per transaction in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
