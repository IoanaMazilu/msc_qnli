consumable_items_premise = 60
consumable_items_hypothesis = 20
clothes_transport_premise = 50
clothes_transport_hypothesis = 50

# the hypothesis talks about the percentage of Mr Yadav's salary spent on consumable items and on clothes and transport - same as in the premise
if consumable_items_premise <= consumable_items_hypothesis:
    # check if the estimate of 'consumable_items_hypothesis' contradicts the percentage of salary spent on consumable items in the premise
    label = "contradiction"
elif clothes_transport_hypothesis != clothes_transport_premise:
    # check if the percentage of salary spent on clothes and transport in the hypothesis contradicts the same percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
