# Premise: 30-Year Mortgage Rates in U.S. Fall Below 4%.
# Hypothesis: 30-year mortgage rates fall below 4% for first time.
# Golden Label: neutral

rate_premise = 4
rate_hypothesis = 4

# the hypothesis and premise mention the mortgage rate
if rate_hypothesis != rate_premise:
    # check if the mortgage rate in the hypothesis contradicts the mortgage rate in the premise
    label = "contradiction"
else:
    # the premise does not mention whether it's the first time the rate falls below 4%, so we cannot infer entailment or contradiction
    label = "neutral"

print(label)

