# Premise: Patrick purchased 70 pencils and sold them at a loss equal to the selling price of 20 pencils.
# Hypothesis: Patrick purchased more than 20 pencils and sold them at a loss equal to the selling price of 20 pencils.
# Golden Label: entailment

pencils_purchased_premise = 70
pencils_purchased_hypothesis = 20
pencils_loss_premise = 20
pencils_loss_hypothesis = 20

# the hypothesis refers to the number of pencils bought and the loss, also mentioned in the premise
if pencils_purchased_premise <= pencils_purchased_hypothesis:
    # check if the estimate of 'pencils_purchased_hypothesis' contradicts the number of pencils purchased in the premise
    label = "contradiction"
elif pencils_loss_hypothesis != pencils_loss_premise:
    # check if the number of sold pencils at a loss in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

