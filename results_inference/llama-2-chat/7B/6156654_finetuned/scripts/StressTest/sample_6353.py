profit_premise = 22000
profit_hypothesis = 22000

# The hypothesis refers to the profit in the business at the end of the year, which is also mentioned in the premise
if profit_hypothesis <= profit_premise:
    # If the hypothesis value is less than or equal to the premise value, it does not contradict the premise
    label = "neutral"
elif profit_hypothesis > profit_premise:
    # If the hypothesis value is greater than the premise value, it contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis value is equal to the premise value, it does not contradict the premise
    label = "entailment"

print(label)
