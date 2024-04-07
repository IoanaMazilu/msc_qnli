# Premise: Vijay sells a cupboard at less than 84% below cost price.
# Hypothesis: Vijay sells a cupboard at 14% below cost price.
# Golden Label: neutral

cupboard_sale_premise = 84
cupboard_sale_hypothesis = 14

# the hypothesis talks about the selling price of the cupboard, referenced also in the premise
if cupboard_sale_hypothesis >= cupboard_sale_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cupboard_sale_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the selling price of the cupboard
    # any selling price less than 'cupboard_sale_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

