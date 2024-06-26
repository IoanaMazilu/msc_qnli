pens_purchased_premise = 12
pens_purchased_hypothesis = 12
cost_premise = 42.00
cost_hypothesis = 42.00

# the hypothesis refers to the number of pens purchased and the cost of the pens, both mentioned in the premise
if pens_purchased_hypothesis <= pens_purchased_premise:
    # check if the hypothesis value contradicts the number of pens purchased in the premise
    label = "contradiction"
elif cost_hypothesis!= cost_premise:
    # check if the cost of the pens in the hypothesis contradicts the cost of the pens in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
