 bought_kiwi_fruit_premise = 8
average_rate_premise = 360
bought_kiwi_fruit_hypothesis = 8
average_rate_hypothesis = 360

# the hypothesis refers to the amount of kiwi fruit bought and the average rate of buying, both mentioned in the premise
if bought_kiwi_fruit_hypothesis!= bought_kiwi_fruit_premise:
    # check if the amount of kiwi fruit bought in the hypothesis contradicts the amount in the premise
    label = "contradiction"
elif average_rate_hypothesis!= average_rate_premise:
    # check if the average rate of buying in the hypothesis contradicts the average rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

