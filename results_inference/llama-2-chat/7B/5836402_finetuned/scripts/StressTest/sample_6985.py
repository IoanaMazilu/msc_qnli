total_pens_premise = 22
total_pens_hypothesis = 12
purchase_price_premise = 42.00
purchase_price_hypothesis = 42.00

# the hypothesis refers to the number of pens and the purchase price, which are also mentioned in the premise
if total_pens_hypothesis >= total_pens_premise:
    # check if the estimate of 'total_pens_hypothesis' contradicts the number of pens in the premise
    label = "contradiction"
elif purchase_price_hypothesis!= purchase_price_premise:
    # check if the purchase price in the hypothesis contradicts the purchase price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
