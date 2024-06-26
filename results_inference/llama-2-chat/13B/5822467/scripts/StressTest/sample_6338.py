wage_premise = 4.00
tip_rate_premise = 0.15
cost_orders_premise = 0.0

wage_hypothesis = 4.00
tip_rate_hypothesis = 0.45
cost_orders_hypothesis = 0.0

# calculate the total earnings for the premise and hypothesis
total_earnings_premise = wage_premise * cost_orders_premise
total_earnings_hypothesis = wage_hypothesis * cost_orders_hypothesis

# check if the hypothesis contradicts the premise
if total_earnings_hypothesis > total_earnings_premise:
    label = "contradiction"
elif total_earnings_hypothesis < total_earnings_premise:
    label = "entailment"
else:
    # the premise and hypothesis values are equal, so the label is neutral
    label = "neutral"

print(label)
