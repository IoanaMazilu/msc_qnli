anup_premise = 7/12
anup_hypothesis = 12/12
t_premise = T

# the hypothesis refers to the fraction of the sum of money T that Anup was asked to find
if anup_hypothesis > anup_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif anup_hypothesis == anup_premise:
    # the hypothesis and premise are the same, no contradiction or entailment
    label = "neutral"
else:
    # the premise gives only a fraction of the sum of money T, the hypothesis is more specific
    # any value of the sum of money T greater than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
