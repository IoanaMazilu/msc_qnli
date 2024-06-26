below_cost_price_premise = 12
below_cost_price_hypothesis = 12

# the hypothesis refers to the below cost price at which Vijay sells a cupboard, also mentioned in the premise
if below_cost_price_hypothesis <= below_cost_price_premise:
    # check if the hypothesis value contradicts the estimate of more than 'below_cost_price_premise'
    label = "contradiction"
else:
    # the premise gives the exact below cost price at which the cupboard is sold
    # any below cost price greater than 'below_cost_price_premise' contradicts the premise
    label = "contradiction"

print(label)
