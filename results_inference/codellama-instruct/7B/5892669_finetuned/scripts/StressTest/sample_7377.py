consumable_items_spending_premise = 60
consumable_items_spending_hypothesis = 20
clothes_transport_spending_premise = 50
clothes_transport_spending_hypothesis = 50

# the hypothesis refers to the spending percentages on consumable items and on clothes and transport mentioned in the premise
if consumable_items_spending_hypothesis >= consumable_items_spending_premise:
    # check if the estimate of 'consumable_items_spending_hypothesis' contradicts the percentage of spending on consumable items in the premise
    label = "contradiction"
elif clothes_transport_spending_hypothesis!= clothes_transport_spending_premise:
    # check if the percentage of spending on clothes and transport in the hypothesis contradicts the percentage of spending on clothes and transport reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)