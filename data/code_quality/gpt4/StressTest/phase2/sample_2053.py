purchase_price_fraction_premise = 5/10
purchase_price_fraction_hypothesis = 9/10
sales_price_increase_premise = 0.08
sales_price_increase_hypothesis = 0.08

# the hypothesis refers to the fraction of the selling price at which Monika purchased the pressure cooker and the percentage increase at which she sold it, as mentioned in the premise
if purchase_price_fraction_hypothesis <= purchase_price_fraction_premise:
    # check if the fraction of the selling price at which Monika allegedly purchased the pressure cooker in the hypothesis contradicts the estimate in the premise
    label = "contradiction"
elif sales_price_increase_hypothesis != sales_price_increase_premise:
    # check if the percentage increase at which Monika allegedly sold the pressure cooker in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # the premise provides an estimate for the fraction of the selling price at which Monika purchased the pressure cooker
    # any fraction greater than 'purchase_price_fraction_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
