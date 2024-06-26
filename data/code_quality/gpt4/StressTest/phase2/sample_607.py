pen_brand_x_price_premise = 5
pen_brand_x_price_hypothesis = 2
pen_brand_y_price_premise = 1
pen_brand_y_price_hypothesis = 1

# the hypothesis refers to the price per pen of both brands mentioned in the premise
if pen_brand_x_price_hypothesis >= pen_brand_x_price_premise:
    # check if the price per pen of brand X in the hypothesis contradicts the estimate of less than 'pen_brand_x_price_premise' in the premise
    label = "contradiction"
elif pen_brand_y_price_hypothesis != pen_brand_y_price_premise:
    # check if the price per pen of brand Y in the hypothesis contradicts the price per pen of brand Y in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
