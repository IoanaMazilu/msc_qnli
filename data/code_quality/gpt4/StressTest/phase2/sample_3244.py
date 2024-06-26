consumable_spending_premise = 40
consumable_spending_hypothesis = 60
clothes_transport_spending_premise = 50
clothes_transport_spending_hypothesis = 50

# the hypothesis refers to the percentages of Mr Yadav's salary spent on consumable items and clothes and transport
if consumable_spending_hypothesis <= consumable_spending_premise:
    # check if the estimate of 'consumable_spending_hypothesis' contradicts the estimate of more than 'consumable_spending_premise'
    label = "contradiction"
elif clothes_transport_spending_hypothesis != clothes_transport_spending_premise:
    # check if the percentage of salary spent on clothes and transport in the hypothesis contradicts the same percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis percentages do not contradict the premise ones, then it is neutral as premise gives only estimate for the consumable spending
    label = "neutral"

print(label)
