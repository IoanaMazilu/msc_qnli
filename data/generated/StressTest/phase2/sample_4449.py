# Premise: 1250, what is Ben's capital?
# Hypothesis: less than 8250, what is Ben's capital?
# Golden Label: entailment

capital_premise = 1250
capital_hypothesis = 8250

# the hypothesis refers to the same capital as the premise
if capital_premise >= capital_hypothesis:
    # check if capital from the premise contradicts the hypothesis of being less than 'capital_hypothesis'
    label = "contradiction"
else:
    # the premise is an exact value, while the hypothesis is an upper bound
    # the premise is consistent with the hypothesis, but cannot be explicitly entailed from it
    label = "neutral"

print(label)

