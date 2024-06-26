consumable_premise = 60
consumable_hypothesis = 40
clothes_transport_premise = 50
clothes_transport_hypothesis = 50

# the hypothesis refers to the percentage of Mr Yadav's monthly salary spent on consumable items and on clothes and transport
if consumable_hypothesis > consumable_premise:
    # check if the estimate of 'consumable_hypothesis' contradicts the percentage spent on consumable items in the premise
    label = "contradiction"
elif clothes_transport_hypothesis != clothes_transport_premise:
    # check if the percentage spent on clothes and transport in the hypothesis contradicts the same percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
