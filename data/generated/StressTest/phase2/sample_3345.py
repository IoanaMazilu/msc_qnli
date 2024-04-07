# Premise: Nitin borrowed some money at the rate of 6% p.
# Hypothesis: Nitin borrowed some money at the rate of less than 8% p.
# Golden Label: entailment

interest_rate_premise = 6
interest_rate_hypothesis = 8

# The hypothesis talks about the interest rate at which Nitin borrowed money, referenced also in the premise
if interest_rate_hypothesis < interest_rate_premise:
    # Check if the hypothesis value contradicts the premise
    label = "contradiction"
elif interest_rate_hypothesis == interest_rate_premise:
    # Check if the hypothesis value is the same as the premise
    label = "entailment"
else:
    # Considering that the interest rate in the premise is less than the one in the hypothesis
    # The premise does not contradict the hypothesis but also does not fully entail it
    label = "neutral"

print(label)

