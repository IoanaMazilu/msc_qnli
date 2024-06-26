joined_premise = "Rs."
joined_hypothesis = "less than 8 months later"
investment_premise = float(joined_premise.split()[1])
investment_hypothesis = float(joined_hypothesis.split()[1])

# Check if the hypothesis value contradicts the estimate in the premise
if investment_hypothesis <= investment_premise:
    label = "contradiction"
elif investment_hypothesis > investment_premise:
    # The hypothesis value is greater than the premise estimate, so we can infer entailment
    label = "entailment"
else:
    # The hypothesis value is equal to the premise estimate, so there is no contradiction or entailment
    label = "neutral"

print(label)
