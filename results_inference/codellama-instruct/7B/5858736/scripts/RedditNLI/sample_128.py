# Extract the numerical information from the premise and hypothesis
premise_amount = 7.2
hypothesis_amount = 7.15

# Check if the amount in the hypothesis contradicts the amount in the premise
if hypothesis_amount!= premise_amount:
    label = "contradiction"
else:
    # If the amount in the hypothesis is consistent with the amount in the premise, we can infer entailment
    label = "entailment"

print(label)
