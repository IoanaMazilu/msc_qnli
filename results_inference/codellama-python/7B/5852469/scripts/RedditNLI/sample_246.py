unemployment_rate_premise = 0.1
unemployment_rate_hypothesis = 0.1

# the hypothesis and premise mention the same unemployment rate
if unemployment_rate_hypothesis!= unemployment_rate_premise:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # the premise and hypothesis mention the same unemployment rate
    # however, the hypothesis does not link the unemployment rate to the US, so we cannot infer entailment
    label = "neutral"

print(label)
