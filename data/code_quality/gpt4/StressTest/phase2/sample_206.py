profit_sreenivas_premise = 10
profit_sreenivas_hypothesis = 80
loss_shiva_premise = 10
loss_shiva_hypothesis = 10

# the hypothesis refers to the profit percentage of Sreenivas and loss percentage of Shiva mentioned in the premise
if profit_sreenivas_premise != profit_sreenivas_hypothesis:
    # check if the profit percentage of Sreenivas in the hypothesis contradicts the profit percentage of Sreenivas in the premise
    label = "contradiction"
elif loss_shiva_premise != loss_shiva_hypothesis:
    # check if the loss percentage of Shiva in the hypothesis contradicts the loss percentage of Shiva in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
