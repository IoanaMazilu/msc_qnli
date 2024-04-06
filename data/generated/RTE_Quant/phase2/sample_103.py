# Premise: Analysts surveyed by Thomson First Call were looking for the company to post earnings of 38 cents per share on sales of $12.81 billion in the latest period.
# Hypothesis: SBC reported earnings of 38 cents per share in the latest quarter.
# Golden Label: neutral

expected_earnings_premise = 0.38
expected_earnings_hypothesis = 0.38

# the hypothesis talks about the actual earnings of the company, while the premise talks about expected earnings
# we cannot infer from the premise whether the actual earnings were indeed as predicted
# therefore, we cannot infer entailment or contradiction from the premise to the hypothesis
label = "neutral"

print(label)

