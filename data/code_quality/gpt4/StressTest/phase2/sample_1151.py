purchased_pencils_premise = 90
purchased_pencils_hypothesis = 40
loss_premise = 40
loss_hypothesis = 40

# The hypothesis refers to the number of purchased pencils and the loss from selling them, which are also mentioned in the premise
if purchased_pencils_hypothesis != purchased_pencils_premise:
    # Check if the number of purchased pencils in the hypothesis contradicts the number of purchased pencils reported in the premise
    label = "contradiction"
elif loss_hypothesis != loss_premise:
    # Check if the loss in the hypothesis contradicts the loss reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
