pens_total_premise = 12
pens_total_hypothesis = 12
pens_price_premise = 42.00
pens_price_hypothesis = 42.00

# the hypothesis refers to the number of pens and their price mentioned in the premise
if pens_total_hypothesis <= pens_total_premise:
    # check if the estimate of 'pens_total_hypothesis' contradicts the number of pens purchased in the premise
    label = "contradiction"
elif pens_price_hypothesis!= pens_price_premise:
    # check if the price of the pens in the hypothesis contradicts the price of the pens reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
