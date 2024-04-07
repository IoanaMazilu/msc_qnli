# Premise: What will be Rakesh’s share in the profit of less than 750000 earned at the end of three years from the start of the business in 1996?
# Hypothesis: What will be Rakesh’s share in the profit of 150000 earned at the end of three years from the start of the business in 1996?
# Golden Label: neutral

profit_premise = 750000
profit_hypothesis = 150000

# the hypothesis refers to the profit earned at the end of three years from 1996
if profit_hypothesis >= profit_premise:
    # check if the amount of profit in the hypothesis contradicts the estimate of less than 'profit_premise'
    label = "contradiction"
elif profit_hypothesis < profit_premise:
    # the premise gives only an estimate for the profit
    # any profit less than 'profit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

