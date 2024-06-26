percentage_premise = [84, 36, 44]
percentage_hypothesis = [64, 36, 44]

# compare the hypothesis values with the premise values
if any(h >= p for h, p in zip(percentage_hypothesis, percentage_premise)):
    # at least one hypothesis value matches a premise value, so contradiction
    label = "contradiction"
else:
    # all hypothesis values are less than or equal to the premise values, so entailment
    label = "entailment"

print(label)
