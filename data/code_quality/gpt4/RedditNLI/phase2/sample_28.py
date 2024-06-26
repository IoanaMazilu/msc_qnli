percentage_elite_premise = .00017
percentage_elite_hypothesis = .00017
spending_premise = 3.5
spending_hypothesis = 2

# the hypothesis and premise both mention a tiny elite group and the amount they control/spend
if percentage_elite_premise != percentage_elite_hypothesis:
    # check if the percentage of the elite group in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif spending_hypothesis > spending_premise:
    # check if the spending amount in the hypothesis contradicts the premise (the premise states the spending is over a certain amount)
    label = "contradiction"
else:
    # if the hypothesis is consistent with the premise but cannot be fully entailed from it, we infer neutrality
    label = "neutral"

print(label)
