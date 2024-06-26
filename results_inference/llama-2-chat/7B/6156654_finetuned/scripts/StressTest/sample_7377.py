consumable_spent_premise = 60
consumable_spent_hypothesis = 20
clothes_transport_premise = 50
clothes_transport_hypothesis = 50

# the hypothesis refers to the percentage of salary spent on consumable items and clothes/transport, which are also mentioned in the premise
if consumable_spent_hypothesis >= consumable_spent_premise:
    label = "contradiction"
elif clothes_transport_hypothesis!= clothes_transport_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
