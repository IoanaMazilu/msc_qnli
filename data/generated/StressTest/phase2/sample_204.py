# Premise: Sreenivas sells a table to Shiva at 10% profit and Shiva sells it to Mahesh at 10% loss.
# Hypothesis: Sreenivas sells a table to Shiva at less than 50% profit and Shiva sells it to Mahesh at 10% loss.
# Golden Label: entailment

profit_sreenivas_premise = 10
profit_sreenivas_hypothesis = 50
loss_shiva_premise = 10
loss_shiva_hypothesis = 10

# the hypothesis refers to the profit and loss percentages mentioned in the premise
if profit_sreenivas_hypothesis < profit_sreenivas_premise:
    # check if the 'profit_sreenivas_hypothesis' contradicts the profit percentage in the premise
    label = "contradiction"
elif loss_shiva_hypothesis != loss_shiva_premise:
    # check if the loss percentage in the hypothesis contradicts the loss percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

