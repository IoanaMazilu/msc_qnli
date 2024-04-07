# Premise: Patrick purchased 80 pencils and sold them at a loss equal to the selling price of 16 pencils.
# Hypothesis: Patrick purchased more than 80 pencils and sold them at a loss equal to the selling price of 16 pencils.
# Golden Label: contradiction

pencils_purchased_premise = 80
pencils_purchased_hypothesis = 80
loss_sales_premise = 16
loss_sales_hypothesis = 16

# the hypothesis talks about the number of purchased pencils and the loss of sales, referenced also in the premise
if pencils_purchased_hypothesis <= pencils_purchased_premise:
    # check if the number of purchased pencils in the hypothesis contradicts the number of purchased pencils reported in the premise
    label = "contradiction"
elif loss_sales_hypothesis != loss_sales_premise:
    # check if the loss of sales in the hypothesis contradicts the loss of sales reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

