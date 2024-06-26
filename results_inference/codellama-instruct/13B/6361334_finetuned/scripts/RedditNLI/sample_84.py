unemployment_rate_premise = 3.9
unemployment_rate_hypothesis = 3.9

# the hypothesis and premise mention the unemployment rate
if unemployment_rate_premise!= unemployment_rate_hypothesis:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # the premise and hypothesis mention the same unemployment rate
    # however, the hypothesis does not mention wage growth, which cannot be entailed from the premise
    label = "neutral"

print(label)
