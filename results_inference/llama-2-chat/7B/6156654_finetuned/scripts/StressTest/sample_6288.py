kiwi_weight_bought_premise = 8
kiwi_weight_bought_hypothesis = 5
average_rate_premise = 360
average_rate_hypothesis = 360

# the hypothesis refers to the weight of kiwi fruit bought by Smitha, which is also mentioned in the premise
if kiwi_weight_bought_hypothesis <= kiwi_weight_bought_premise:
    # check if the weight of kiwi fruit in the hypothesis contradicts the weight of kiwi fruit in the premise
    label = "contradiction"
elif average_rate_hypothesis!= average_rate_premise:
    # check if the average rate of kiwi fruit in the hypothesis contradicts the average rate of kiwi fruit in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
