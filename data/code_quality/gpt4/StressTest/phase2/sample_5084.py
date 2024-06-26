hourly_wage_premise = 7.00
hourly_wage_hypothesis = 7.00
tip_rate_premise = 5
tip_rate_hypothesis = 5

# The hypothesis refers to the hourly wage and tip rate mentioned in the premise
if hourly_wage_premise != hourly_wage_hypothesis:
    # Check if the hourly wage in the hypothesis contradicts the hourly wage reported in the premise
    label = "contradiction"
elif tip_rate_hypothesis <= tip_rate_premise:
    # Check if the tip rate in the hypothesis contradicts the tip rate given in the premise
    label = "contradiction"
else:
    # If the hourly wage and tip rate in the hypothesis do not contradict the premise, but cannot be explicitly confirmed by the premise
    label = "neutral"

print(label)
