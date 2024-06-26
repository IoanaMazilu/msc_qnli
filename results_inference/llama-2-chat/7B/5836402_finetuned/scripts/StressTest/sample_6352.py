profit_premise = 42000
profit_hypothesis = 22000

# the hypothesis refers to the profit in the business at the end of the year mentioned in the premise
if profit_hypothesis >= profit_premise:
    # check if the hypothesis value contradicts the estimate of less than 'profit_premise'
    label = "contradiction"
elif profit_hypothesis < profit_premise:
    # if the hypothesis value is less than the premise, it is entailed
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise, it is neutral
    label = "neutral"

print(label)
