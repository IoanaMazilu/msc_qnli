price_reduction_premise = 15
price_reduction_hypothesis = 55
sale_price_premise = 1275
sale_price_hypothesis = 1275

# the hypothesis refers to the same computer sale situation described in the premise

if price_reduction_hypothesis < price_reduction_premise:
    # check if the price reduction percentage in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif sale_price_hypothesis != sale_price_premise:
    # check if the sale price in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
