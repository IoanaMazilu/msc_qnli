hourly_wage_premise = 10.00
hourly_wage_hypothesis = 10.00
tip_rate_premise = 40
tip_rate_hypothesis = 80

# the hypothesis refers to the same hourly wage and tip rate as the premise
if hourly_wage_hypothesis!= hourly_wage_premise:
    label = "contradiction"
elif tip_rate_hypothesis < tip_rate_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
