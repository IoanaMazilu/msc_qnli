earnings_premise = 358
earnings_hypothesis = 558

# the hypothesis refers to the earnings of Michael last week, which is also mentioned in the premise
if earnings_hypothesis != earnings_premise:
    # check if the earnings in the hypothesis contradicts the earnings reported in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are the same so we can infer entailment
    label = "entailment"

print(label)
