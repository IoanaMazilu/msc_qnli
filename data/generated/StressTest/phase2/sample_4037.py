# Premise: Patrick purchased 80 pencils and sold them at a loss equal to the selling price of 30 pencils.
# Hypothesis: Patrick purchased less than 80 pencils and sold them at a loss equal to the selling price of 30 pencils.
# Golden Label: contradiction

pencils_purchased_premise = 80
loss_value_premise = 30
pencils_purchased_hypothesis = 80
loss_value_hypothesis = 30

# the hypothesis refers to the number of pencils purchased and the loss incurred, mentioned in the premise
if pencils_purchased_hypothesis >= pencils_purchased_premise:
    # check if the hypothesis value contradicts the number of pencils purchased in the premise
    label = "contradiction"
elif loss_value_hypothesis != loss_value_premise:
    # check if the loss value in the hypothesis contradicts the loss value reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

