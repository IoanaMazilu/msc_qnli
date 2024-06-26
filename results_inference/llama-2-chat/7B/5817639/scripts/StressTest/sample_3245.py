# define variables for premise and hypothesis
consumable_premise = 60
consumable_hypothesis = 60
clothes_transport_premise = 50
clothes_transport_hypothesis = 50

# compare the hypothesis with the premise
if clothes_transport_hypothesis > clothes_transport_premise:
    # check if the estimate of 'clothes_transport_hypothesis' contradicts the number of clothes and transport reported in the premise
    label = "contradiction"
elif consumable_hypothesis > consumable_premise:
    # check if the estimate of 'consumable_hypothesis' contradicts the number of consumable items reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
