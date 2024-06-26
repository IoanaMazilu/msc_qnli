profit_premise = 42000
profit_hypothesis = 22000

# the hypothesis refers to the profit in the business at the end of the year mentioned in the premise
if profit_hypothesis >= profit_premise:
    # check if the profit in the hypothesis contradicts the premise (less than 42000)
    label = "contradiction"
elif profit_hypothesis < profit_premise:
    # the profit in the hypothesis is less than the profit in the premise
    # it does not contradict the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
