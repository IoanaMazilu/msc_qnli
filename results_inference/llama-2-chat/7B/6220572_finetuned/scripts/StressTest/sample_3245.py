consumable_items_premise = 60
consumable_items_hypothesis = 60
clothes_transport_premise = 50
clothes_transport_hypothesis = 50

# the hypothesis refers to the percentages of salary spent on different items, also mentioned in the premise
if consumable_items_hypothesis >= consumable_items_premise:
    # check if the estimate of 'consumable_items_hypothesis' contradicts the percentage of salary spent on consumable items in the premise
    label = "contradiction"
elif clothes_transport_hypothesis!= clothes_transport_premise:
    # check if the number of spent on clothes and transport in the hypothesis contradicts the number of spent on clothes and transport reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
