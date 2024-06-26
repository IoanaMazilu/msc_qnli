consumable_spending_premise = 0.6
consumable_spending_hypothesis = 0.6
clothes_transport_spending_premise = 0.5
clothes_transport_spending_hypothesis = 0.5

# the hypothesis refers to the percentage of monthly salary spent on consumable items and clothes/transport, mentioned in the premise
if consumable_spending_hypothesis >= consumable_spending_premise:
    # check if the estimate of 'consumable_spending_hypothesis' contradicts the percentage of salary spent on consumable items in the premise
    label = "contradiction"
elif clothes_transport_spending_hypothesis!= clothes_transport_spending_premise:
    # check if the percentage of salary spent on clothes and transport in the hypothesis contradicts the percentage of salary spent on clothes and transport in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
