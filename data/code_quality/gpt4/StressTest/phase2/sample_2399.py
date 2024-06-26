consumable_spending_premise = 60
consumable_spending_hypothesis = 60
clothes_transport_spending_premise = 50
clothes_transport_spending_hypothesis = 50

# the hypothesis refers to the percentage of Mr Yadav's salary spent on consumable items and on clothes and transport
# these are the same percentages mentioned in the premise
if consumable_spending_hypothesis > consumable_spending_premise:
    # check if the hypothesis's claim of 'more than 60%' contradicts the percentage of salary spent on consumable items in the premise
    label = "contradiction"
elif clothes_transport_spending_hypothesis != clothes_transport_spending_premise:
    # check if the percentage of salary spent on clothes and transport in the hypothesis contradicts the same percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis percentages do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
