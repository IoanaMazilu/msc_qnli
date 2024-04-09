premise_amount = 5.1 * 1000000000  # convert the premise amount to a float
hypothesis_amount = 5.1 * 1000000000  # convert the hypothesis amount to a float

# check if the amount in the hypothesis contradicts the amount in the premise
if hypothesis_amount!= premise_amount:
    label = "contradiction"
elif hypothesis_amount > premise_amount:
    label = "entailment"
else:
    label = "neutral"

print(label)
