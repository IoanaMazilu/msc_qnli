pens_purchased_premise = 12
pens_purchased_hypothesis = 12

# the hypothesis refers to the number of pens purchased by Elena mentioned in the premise
if pens_purchased_hypothesis <= pens_purchased_premise:
    # check if the estimate of 'pens_purchased_hypothesis' contradicts the number of pens purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
