pens_purchased_premise = 12
pens_purchased_hypothesis = 12
total_purchase_premise = 42.00
total_purchase_hypothesis = 42.00

# the hypothesis talks about the number of pens purchased, which is also mentioned in the premise
if pens_purchased_hypothesis <= pens_purchased_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif total_purchase_hypothesis!= total_purchase_premise:
    # check if the total purchase in the hypothesis contradicts the total purchase in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
