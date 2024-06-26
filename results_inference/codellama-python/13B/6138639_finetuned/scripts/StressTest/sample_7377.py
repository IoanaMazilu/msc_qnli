consumable_items_percentage_premise = 60
consumable_items_percentage_hypothesis = 20
clothes_transport_percentage_premise = 50
clothes_transport_percentage_hypothesis = 50

# the hypothesis refers to the percentage of Mr Yadav's monthly salary spent on consumable items and clothes and transport, mentioned in the premise
if consumable_items_percentage_premise <= consumable_items_percentage_hypothesis:
    # check if the estimate of 'consumable_items_percentage_hypothesis' contradicts the percentage of consumable items in the premise
    label = "contradiction"
elif clothes_transport_percentage_hypothesis!= clothes_transport_percentage_premise:
    # check if the percentage of clothes and transport in the hypothesis contradicts the percentage of clothes and transport reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
