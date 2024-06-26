wage_premise = 6.00
tip_rate_premise = 0.35
hours_worked_premise = 4
orders_served_premise = 20

wage_hypothesis = 6.00
tip_rate_hypothesis = 0.65
hours_worked_hypothesis = 4
orders_served_hypothesis = 25

# calculate the total earnings for the premise and hypothesis
total_earnings_premise = wage_premise * hours_worked_premise + (orders_served_premise * tip_rate_premise)
total_earnings_hypothesis = wage_hypothesis * hours_worked_hypothesis + (orders_served_hypothesis * tip_rate_hypothesis)

# compare the total earnings
if total_earnings_premise > total_earnings_hypothesis:
    label = "entailment"
elif total_earnings_hypothesis > total_earnings_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
