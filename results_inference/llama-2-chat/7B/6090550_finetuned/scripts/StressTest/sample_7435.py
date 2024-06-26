item_price_premise = 70
item_price_hypothesis = 90
tax_rate_premise = 0.20
tax_rate_hypothesis = 0.20
rebate_amount_premise = 10
rebate_amount_hypothesis = 10

# the hypothesis refers to the same situation as the premise, but with different item prices
if item_price_hypothesis <= item_price_premise:
    # check if the hypothesis value contradicts the premise's estimate of more than 'item_price_premise'
    label = "contradiction"
elif tax_rate_hypothesis!= tax_rate_premise or rebate_amount_hypothesis!= rebate_amount_premise:
    # check if the tax rate or rebate amount in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis values do not contradict the premise ones, but they are not explicitly entailed either
    label = "neutral"

print(label)
