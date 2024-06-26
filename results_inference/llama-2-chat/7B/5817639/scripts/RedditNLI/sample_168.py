# Define variables for the premise and hypothesis
premise_amount = 363
hypothesis_amount = 215

# Check if the amount in the hypothesis contradicts the premise
if hypothesis_amount < premise_amount:
    label = "contradiction"
else:
    # If the amounts are the same or the hypothesis amount is greater than the premise amount, we can infer entailment
    label = "entailment"
else:
    # If the amounts are different and the hypothesis amount is not greater than the premise amount, we cannot explicitly entail the hypothesis from the premise
    label = "neutral"

print(label)
