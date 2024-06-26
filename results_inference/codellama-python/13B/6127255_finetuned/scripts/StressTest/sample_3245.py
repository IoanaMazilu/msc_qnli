consumable_items_premise = 60
consumable_items_hypothesis = 60
clothes_transport_premise = 50
clothes_transport_hypothesis = 50

# the hypothesis refers to the percentage of Mr Yadav's salary spent on consumable items and on clothes and transport
if consumable_items_hypothesis >= consumable_items_premise:
    # check if the hypothesis value contradicts the premise value for consumable items
    label = "contradiction"
elif clothes_transport_hypothesis!= clothes_transport_premise:
    # check if the percentage spent on clothes and transport according to the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
