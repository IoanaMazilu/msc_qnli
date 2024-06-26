consumable_items_spending_premise = 60
consumable_items_spending_hypothesis = 10
clothes_transport_spending_premise = 50
clothes_transport_spending_hypothesis = 50

# the hypothesis refers to the same spending as the premise
if consumable_items_spending_hypothesis != consumable_items_spending_premise:
    # check if the percentage of salary spent on consumable items in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
elif clothes_transport_spending_hypothesis != clothes_transport_spending_premise:
    # check if the percentage of the remaining salary spent on clothes and transport in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
