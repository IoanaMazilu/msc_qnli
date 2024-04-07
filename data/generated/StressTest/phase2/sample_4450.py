# Premise: less than 8250, what is Ben's capital?
# Hypothesis: 1250, what is Ben's capital?
# Golden Label: neutral

bens_capital_premise = 8250
bens_capital_hypothesis = 1250

# the hypothesis refers to Ben's capital mentioned in the premise
if bens_capital_hypothesis >= bens_capital_premise:
    # check if the value of 'bens_capital_hypothesis' contradicts the estimate of less than 'bens_capital_premise'
    label = "contradiction"
elif bens_capital_hypothesis < bens_capital_premise:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)

