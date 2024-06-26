investment_premise = 620000
investment_hypothesis = 120000

# The hypothesis refers to the investment made in 6 months mentioned in the premise
if investment_hypothesis >= investment_premise:
    # Check if the amount of 'investment_hypothesis' contradicts the premise's statement of less than 'investment_premise'
    label = "contradiction"
elif investment_hypothesis == investment_premise:
    # If the hypothesis amount matches the premise amount, it would be an entailment
    label = "entailment"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we cannot infer entailment or contradiction, thus it is neutral
    label = "neutral"

print(label)
