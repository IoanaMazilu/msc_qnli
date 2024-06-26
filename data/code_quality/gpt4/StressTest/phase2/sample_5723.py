pencils_purchased_premise = 70
pencils_purchased_hypothesis = 70
loss_premise = 20
loss_hypothesis = 20

# the hypothesis refers to the number of pencils purchased and the loss incurred by Patrick, both mentioned in the premise
if pencils_purchased_hypothesis >= pencils_purchased_premise:
    # check if the number of pencils in the hypothesis contradicts the premise
    label = "contradiction"
elif loss_hypothesis != loss_premise:
    # check if the loss in the hypothesis contradicts the loss reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
