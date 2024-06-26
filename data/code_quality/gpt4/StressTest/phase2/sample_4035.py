pencils_purchased_premise = 80
pencils_purchased_hypothesis = 10
loss_premise = 30
loss_hypothesis = 30

# the hypothesis refers to the number of pencils purchased and the loss incurred on sale, mentioned in the premise
if pencils_purchased_premise <= pencils_purchased_hypothesis:
    # check if the estimate of 'pencils_purchased_hypothesis' contradicts the number of pencils purchased as per the premise
    label = "contradiction"
elif loss_premise != loss_hypothesis:
    # check if the loss incurred on sale as per the hypothesis contradicts the loss reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
