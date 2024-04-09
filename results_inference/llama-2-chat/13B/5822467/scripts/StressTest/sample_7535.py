leo_gain_premise = 10
leo_gain_hypothesis = 80
kendra_weight_premise = 50

# the hypothesis refers to the amount of weight Leo gains and the relationship between his weight and Kendra's weight
if leo_gain_hypothesis <= (1 + 0.5)*kendra_weight_premise:
    # check if the estimate of 'leo_gain_hypothesis' contradicts the relationship between Leo and Kendra's weight in the premise
    label = "contradiction"
elif leo_gain_hypothesis!= (1 + 0.5)*kendra_weight_premise:
    # check if the weight of Leo in the hypothesis contradicts the relationship between Leo and Kendra's weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
