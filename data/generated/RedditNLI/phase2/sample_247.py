# Premise: Unemployment rate plunges to 7.8%-WaPo.
# Hypothesis: Unemployment below 8%.
# Golden Label: entailment

unemployment_rate_premise = 7.8
unemployment_rate_hypothesis = 8

# the hypothesis and premise mention the unemployment rate
if unemployment_rate_hypothesis <= unemployment_rate_premise:
    # check if the unemployment rate in the hypothesis is consistent with the unemployment rate in the premise
    label = "entailment"
else:
    # the unemployment rate in the hypothesis is higher than the premise's rate
    label = "contradiction"

print(label)

