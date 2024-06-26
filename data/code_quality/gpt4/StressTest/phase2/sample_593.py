consumable_items_premise = 60
consumable_items_hypothesis = 40
clothes_transport_premise = 50
clothes_transport_hypothesis = 50

# the hypothesis refers to the percentages of Mr Yadav's salary spent on consumable items and on clothes and transport
if consumable_items_premise != consumable_items_hypothesis:
    # check if the percentage spent on consumable items in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
elif clothes_transport_hypothesis != clothes_transport_premise:
    # check if the percentage spent on clothes and transport in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentages do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
