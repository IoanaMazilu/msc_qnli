# Premise: Calculate and compare the maturity values of $1000 invested in each type of GIC.
# Hypothesis: Calculate and compare the maturity values of $more than 1000 invested in each type of GIC.
# Golden Label: contradiction

investment_premise = 1000
investment_hypothesis = 1000

# the hypothesis refers to the amount invested in GICs mentioned in the premise
if investment_hypothesis < investment_premise:
    # check if the hypothesis value contradicts the premise's investment value
    label = "contradiction"
elif investment_hypothesis == investment_premise:
    # if the hypothesis value and the premise value are the same, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value is larger than the premise value, the relation is neutral
    label = "neutral"

print(label)

