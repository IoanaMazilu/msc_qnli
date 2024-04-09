hourly_wage_premise = 1.5 * x / 11 for hours <= 11
hourly_wage_hypothesis = 1.5 * x / 21 for hours <= 21

# check if the hypothesis value contradicts the estimate of the premise
if hourly_wage_hypothesis <= hourly_wage_premise:
    label = "contradiction"
elif hourly_wage_hypothesis > hourly_wage_premise:
    # the hypothesis value is greater than the premise estimate, but we cannot infer entailment
    label = "neutral"
else:
    # the premise estimate is less than the hypothesis value, so we can infer entailment
    label = "entailment"

print(label)
