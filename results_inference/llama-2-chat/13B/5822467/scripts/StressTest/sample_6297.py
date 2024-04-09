hourly_wage_premise = 12 * x + (1.5 * x) * (12 - 82)
hourly_wage_hypothesis = 12 * x + (1.5 * x) * (82 - 12)

# check if the hypothesis value contradicts the estimate of the premise
if hourly_wage_hypothesis <= hourly_wage_premise:
    label = "contradiction"
elif hourly_wage_premise!= hourly_wage_hypothesis:
    label = "neutral"
else:
    label = "entailment"

print(label)
