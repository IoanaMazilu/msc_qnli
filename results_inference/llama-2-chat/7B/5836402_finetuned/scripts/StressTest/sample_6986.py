pens_purchased_premise = 12
pens_purchased_hypothesis = 12
price_premise = 42.00
price_hypothesis = 42.00

# the hypothesis refers to the number of pens and price mentioned in the premise
if pens_purchased_hypothesis <= pens_purchased_premise:
    # check if the hypothesis value contradicts the estimate of more than 'pens_purchased_premise'
    label = "contradiction"
elif price_hypothesis!= price_premise:
    # check if the price in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
