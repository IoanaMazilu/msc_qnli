pencils_purchased_premise = 60
pencils_purchased_hypothesis = 50
loss_premise = 20
loss_hypothesis = 20

# the hypothesis refers to the number of purchased pencils and the loss, which are both mentioned in the premise
if pencils_purchased_premise <= pencils_purchased_hypothesis:
    # check if the hypothesis estimate contradicts the number of purchased pencils in the premise
    label = "contradiction"
elif loss_premise != loss_hypothesis:
    # check if the loss in the hypothesis contradicts the loss reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
