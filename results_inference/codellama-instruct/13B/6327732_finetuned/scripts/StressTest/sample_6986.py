total_pens_premise = 12
total_pens_hypothesis = 12
price_pens_premise = 42.00
price_pens_hypothesis = 42.00

# the hypothesis refers to the number of pens purchased and the price mentioned in the premise
if total_pens_hypothesis <= total_pens_premise:
    # check if the estimate of 'total_pens_hypothesis' contradicts the number of pens purchased in the premise
    label = "contradiction"
elif price_pens_hypothesis!= price_pens_premise:
    # check if the price in the hypothesis contradicts the price mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
