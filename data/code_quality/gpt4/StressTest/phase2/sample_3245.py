consumable_items_premise = 60
consumable_items_hypothesis = 60
clothes_transport_premise = 50
clothes_transport_hypothesis = 50

# the hypothesis talks about the percentages of Mr Yadav's salary spent on consumable items and on clothes and transport
if consumable_items_hypothesis >= consumable_items_premise:
    # check if the hypothesis estimation contradicts the percentage spent on consumable items in the premise
    label = "contradiction"
elif clothes_transport_hypothesis != clothes_transport_premise:
    # check if the percentage spent on clothes and transport in the hypothesis contradicts the percentage spent on clothes and transport in the premise
    label = "contradiction"
else:
    # if the hypothesis percentages do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
