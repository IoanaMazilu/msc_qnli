premise_amount = 10000
hypothesis_amount = 10000

if hypothesis_amount > premise_amount:
    # check if the amount in the hypothesis is greater than the amount in the premise
    label = "contradiction"
elif hypothesis_amount == premise_amount:
    # check if the amount in the hypothesis is equal to the amount in the premise
    label = "entailment"
else:
    # if the amount in the hypothesis is less than the amount in the premise, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
