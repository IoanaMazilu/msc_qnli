wage_premise = 8.00
tip_rate_premise = 0.30
hourly_earnings_premise = wage_premise + (tip_rate_premise * wage_premise)
hypothesis_wage = 8.00
hypothesis_tip_rate = 0.25
hourly_earnings_hypothesis = hypothesis_wage + (hypothesis_tip_rate * hypothesis_wage)

# compare the hourly earnings in the premise and hypothesis
if hourly_earnings_premise <= hourly_earnings_hypothesis:
    # the hypothesis hourly earnings is less than or equal to the premise hourly earnings, so there is no contradiction
    label = "neutral"
elif hourly_earnings_hypothesis!= hourly_earnings_premise:
    # the hypothesis hourly earnings is different from the premise hourly earnings, so there is a contradiction
    label = "contradiction"
else:
    # the hypothesis hourly earnings is greater than the premise hourly earnings, so there is entailment
    label = "entailment"

print(label)
