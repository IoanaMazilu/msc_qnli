consumable_premise = 60
consumable_hypothesis = 20
clothes_transport_premise = 50
clothes_transport_hypothesis = 50

# the hypothesis talks about the percentage of salary spent on consumable items and clothes/transport, referenced also in the premise
if consumable_hypothesis <= consumable_premise:
    # check if the hypothesis value contradicts the estimate of 'consumable_premise'
    label = "contradiction"
elif clothes_transport_hypothesis!= clothes_transport_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
