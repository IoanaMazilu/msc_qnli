expected_earnings_premise = 0.38
expected_earnings_hypothesis = 0.38

# the hypothesis talks about the actual earnings of the company, while the premise talks about expected earnings
# we cannot infer from the premise whether the actual earnings were indeed as predicted
# therefore, we cannot infer entailment or contradiction from the premise to the hypothesis
label = "neutral"

print(label)
