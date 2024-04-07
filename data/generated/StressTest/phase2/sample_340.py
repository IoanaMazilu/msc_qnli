# Premise: less than 620000 for 6 months, whereas Dave invested his amount for the whole yr, what was the amount invested by Dave?
# Hypothesis: 120000 for 6 months, whereas Dave invested his amount for the whole yr, what was the amount invested by Dave?
# Golden Label: neutral

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

