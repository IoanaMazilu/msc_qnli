monthly_salary_premise = 60
consumable_items_premise = 20
clothes_transport_premise = 50

monthly_salary_hypothesis = 20
consumable_items_hypothesis = 50
clothes_transport_hypothesis = 50

# the hypothesis refers to the percentage of monthly salary spent on consumable items and clothes and transport
if consumable_items_hypothesis > consumable_items_premise:
    # check if the estimate of 'consumable_items_hypothesis' contradicts the percentage of monthly salary spent on consumable items in the premise
    label = "contradiction"
elif clothes_transport_hypothesis!= clothes_transport_premise:
    # check if the percentage of monthly salary spent on clothes and transport in the hypothesis contradicts the percentage of monthly salary spent on clothes and transport reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
