# Premise: Store Z:$more than 60, a 30% sales tax, and $10 rebate after tax Isaac can purchase a certain item in four different ways, as shown in the table.
# Hypothesis: Store Z:$70, a 30% sales tax, and $10 rebate after tax Isaac can purchase a certain item in four different ways, as shown in the table.
# Golden Label: neutral

price_premise = 60
price_hypothesis = 70
tax_rate = 30
rebate = 10

# the hypothesis talks about the price of an item in Store Z, the sales tax, and the rebate after tax
# all these quantities are also mentioned in the premise
if price_hypothesis <= price_premise:
    # check if the price in the hypothesis contradicts the estimate of 'more than 60'
    label = "contradiction"
else:
    # the premise gives only an estimate for the price of the item
    # any price greater than 'price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

