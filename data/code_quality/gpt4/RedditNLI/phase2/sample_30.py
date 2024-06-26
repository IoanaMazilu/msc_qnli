percentage_elite_premise = 0.00017
percentage_elite_hypothesis = 0.00017
amount_premise = 2
amount_hypothesis = 3.5

# the hypothesis and premise mention a small proportion of the elite and a large amount of money
if percentage_elite_premise != percentage_elite_hypothesis:
    # check if the percentage of the elite in the hypothesis contradicts the percentage of the elite in the premise
    label = "contradiction"
elif amount_hypothesis < amount_premise:
    # check if the amount in the hypothesis contradicts the premise estimate of over 'amount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money
    # any estimate of the amount in the hypothesis greater or equal to 'amount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
