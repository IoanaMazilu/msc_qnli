# Premise: Patrick purchased more than 50 pencils and sold them at a loss equal to the selling price of 16 pencils.
# Hypothesis: Patrick purchased 80 pencils and sold them at a loss equal to the selling price of 16 pencils.
# Golden Label: neutral

pencils_purchased_premise = 50
pencils_purchased_hypothesis = 80
pencils_loss_premise = 16
pencils_loss_hypothesis = 16

# the hypothesis refers to the number of purchased pencils and the loss of pencils mentioned in the premise
if pencils_purchased_hypothesis <= pencils_purchased_premise:
    # check if the hypothesis value contradicts the estimate of more than 'pencils_purchased_premise'
    label = "contradiction"
elif pencils_loss_hypothesis != pencils_loss_premise:
    # check if the number of loss in the hypothesis contradicts the number of loss reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of purchased pencils
    # any number of purchased pencils greater than 'pencils_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

