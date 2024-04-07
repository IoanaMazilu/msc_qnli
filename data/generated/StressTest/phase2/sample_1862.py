# Premise: Patrick purchased 60 pencils and sold them at a loss equal to the selling price of 20 pencils.
# Hypothesis: Patrick purchased 80 pencils and sold them at a loss equal to the selling price of 20 pencils.
# Golden Label: contradiction

pencils_purchased_premise = 60
pencils_purchased_hypothesis = 80
loss_premise = 20
loss_hypothesis = 20

# the hypothesis refers to the number of purchased pencils and the loss mentioned in the premise
if pencils_purchased_premise != pencils_purchased_hypothesis:
    # check if the number of purchased pencils in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif loss_premise != loss_hypothesis:
    # check if the loss in the hypothesis contradicts the loss reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

