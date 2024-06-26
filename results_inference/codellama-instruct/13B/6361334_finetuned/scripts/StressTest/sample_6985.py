total_pens_premise = 22
total_pens_hypothesis = 12
price_per_pen_premise = 42.00
price_per_pen_hypothesis = 42.00

# the hypothesis refers to the number of pens purchased and the price per pen, both mentioned in the premise
if total_pens_hypothesis <= total_pens_premise:
    # check if the hypothesis value contradicts the estimate of less than 'total_pens_premise'
    label = "contradiction"
elif price_per_pen_hypothesis!= price_per_pen_premise:
    # check if the price per pen in the hypothesis contradicts the price per pen reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
