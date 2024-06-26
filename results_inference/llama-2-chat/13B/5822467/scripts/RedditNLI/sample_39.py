surplus_premise = 0.93 * 10^9  # convert JPY trillion to number
surplus_hypothesis = 7.01 * 10^9  # convert USD billion to number

# check if the hypothesis surplus is greater than the premise surplus
if surplus_hypothesis > surplus_premise:
    label = "entailment"
elif surplus_premise > surplus_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
