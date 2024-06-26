consumable_items_percentage_premise = 60
consumable_items_percentage_hypothesis = 60
clothes_and_transport_percentage_premise = 50
clothes_and_transport_percentage_hypothesis = 50

# the hypothesis refers to the percentage of Mr Yadav's monthly salary spent on consumable items and clothes and transport, mentioned in the premise
if consumable_items_percentage_hypothesis >= consumable_items_percentage_premise:
    # check if the hypothesis value contradicts the estimate of less than 'consumable_items_percentage_premise'
    label = "contradiction"
elif clothes_and_transport_percentage_hypothesis!= clothes_and_transport_percentage_premise:
    # check if the percentage of clothes and transport in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
