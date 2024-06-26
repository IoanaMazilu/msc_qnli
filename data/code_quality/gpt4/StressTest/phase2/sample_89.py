deposit_premise = 67600
deposit_hypothesis = 47600
interest_rate = 16

# the hypothesis refers to the same deposit amount and interest rate as in the premise
if deposit_hypothesis > deposit_premise:
    # if the deposit amount in the hypothesis is more than the deposit amount in the premise, it contradicts the premise
    label = "contradiction"
elif deposit_hypothesis < deposit_premise:
    # if the deposit amount in the hypothesis is less than the deposit amount in the premise, it contradicts the premise
    label = "contradiction"
else:
    # if the deposit amount and the interest rate in the hypothesis match the premise, we can infer entailment
    label = "entailment"

print(label)
