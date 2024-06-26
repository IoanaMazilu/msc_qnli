earnings_premise = 210
earnings_hypothesis = 210

# the hypothesis refers to the earnings of Michael mentioned in the premise
if earnings_hypothesis != earnings_premise:
    # if the earnings in the hypothesis are different than the earnings in the premise, we have a contradiction
    label = "contradiction"
else:
    # if the earnings in the hypothesis are the same as the earnings in the premise, we have entailment
    label = "entailment"

print(label)
