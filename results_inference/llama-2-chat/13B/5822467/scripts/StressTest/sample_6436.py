wage_premise = 6.00
tip_rate_premise = 0.75
hours_worked_premise = 1
orders_served_premise = 10

wage_hypothesis = 6.00
tip_rate_hypothesis = 0.35
hours_worked_hypothesis = 1
orders_served_hypothesis = 10

# calculate total earnings from the premise
total_earnings_premise = wage_premise * hours_worked_premise + (orders_served_premise * tip_rate_premise * hours_worked_premise)

# calculate total earnings from the hypothesis
total_earnings_hypothesis = wage_hypothesis * hours_worked_hypothesis + (orders_served_hypothesis * tip_rate_hypothesis * hours_worked_hypothesis)

# compare the total earnings from the premise and hypothesis
if total_earnings_premise > total_earnings_hypothesis:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif total_earnings_premise < total_earnings_hypothesis:
    # the premise contradicts the hypothesis
    label = "contradiction"
else:
    # the total earnings from the premise and hypothesis are the same
    label = "neutral"

print(label)
