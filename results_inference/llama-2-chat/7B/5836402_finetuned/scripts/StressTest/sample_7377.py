consumable_spend_premise = 0.6
consumable_spend_hypothesis = 0.2
clothes_transport_premise = 0.5
clothes_transport_hypothesis = 0.5

# the hypothesis refers to the percentage of Mr Yadav's monthly salary spent on consumable items and clothes and transport, mentioned in the premise
if consumable_spend_premise >= consumable_spend_hypothesis:
    # check if the estimate of 'consumable_spend_hypothesis' contradicts the percentage of consumable items spent in the premise
    label = "contradiction"
elif clothes_transport_hypothesis!= clothes_transport_premise:
    # check if the percentage of clothes and transport in the hypothesis contradicts the percentage of clothes and transport reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
