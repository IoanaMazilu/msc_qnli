crayons_premise = float(7.0)
crayons_hypothesis = float(10.0)

# compare the number of crayons in the premise and hypothesis
if crayons_hypothesis > crayons_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif crayons_hypothesis == crayons_premise:
    # the hypothesis and premise values are the same, no entailment or contradiction
    label = "neutral"
else:
    # the hypothesis values are greater than the premise values, entailment
    label = "entailment"

print(label)
