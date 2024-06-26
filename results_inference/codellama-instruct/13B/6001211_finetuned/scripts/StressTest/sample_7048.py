cupboard_sale_premise = 62
cupboard_sale_hypothesis = 12

# the hypothesis refers to the selling price of the cupboard, which is also mentioned in the premise
if cupboard_sale_hypothesis >= cupboard_sale_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cupboard_sale_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the selling price of the cupboard
    # any selling price less than 'cupboard_sale_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
