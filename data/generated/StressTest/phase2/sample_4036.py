# Premise: Patrick purchased more than 10 pencils and sold them at a loss equal to the selling price of 30 pencils.
# Hypothesis: Patrick purchased 80 pencils and sold them at a loss equal to the selling price of 30 pencils.
# Golden Label: neutral

pencils_purchased_premise = 10
pencils_purchased_hypothesis = 80
loss_premise = 30
loss_hypothesis = 30

# the hypothesis refers to the number of purchased pencils and the loss from selling them, mentioned in the premise
if pencils_purchased_hypothesis <= pencils_purchased_premise:
    # check if the number of pencils Patrick purchased according to the hypothesis contradicts the premise
    label = "contradiction"
elif loss_hypothesis != loss_premise:
    # check if the loss from selling the pencils according to the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pencils purchased
    # any number greater than 'pencils_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

