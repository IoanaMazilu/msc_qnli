# Premise: What will be Rakesh’s share in the profit of 150000 earned at the end of three years from the start of the business in 1996?
# Hypothesis: What will be Rakesh’s share in the profit of less than 750000 earned at the end of three years from the start of the business in 1996?
# Golden Label: entailment

profit_premise = 150000
profit_hypothesis = 750000

# the hypothesis refers to the profit share of Rakesh, mentioned also in the premise
if profit_hypothesis < profit_premise:
    # check if the estimate of 'profit_hypothesis' contradicts the profit in the premise
    label = "contradiction"
elif profit_hypothesis == profit_premise:
    # if the profit in the hypothesis is equal to the profit in the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives an exact amount for the profit
    # any profit less than 'profit_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

