pencils_purchased_premise = 90
pencils_purchased_hypothesis = 50
loss_premise = 40
loss_hypothesis = 40

# the hypothesis refers to the number of pencils purchased and the loss mentioned in the premise
if pencils_purchased_premise <= pencils_purchased_hypothesis:
    # check if the estimate of 'pencils_purchased_hypothesis' contradicts the number of purchased pencils in the premise
    label = "contradiction"
elif loss_hypothesis != loss_premise:
    # check if the loss in the hypothesis contradicts the loss reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
