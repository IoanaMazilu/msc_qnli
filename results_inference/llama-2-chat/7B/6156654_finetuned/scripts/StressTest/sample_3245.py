consumable_percentage_premise = 60
consumable_percentage_hypothesis = 60
clothes_transport_percentage_premise = 50
clothes_transport_percentage_hypothesis = 50

# the hypothesis refers to the same percentages as the premise
if consumable_percentage_hypothesis >= consumable_percentage_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif clothes_transport_percentage_hypothesis!= clothes_transport_percentage_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
