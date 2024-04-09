fruit_weight_premise = 8
fruit_weight_hypothesis = 8
avg_rate_premise = 360
avg_rate_hypothesis = 360

# the hypothesis refers to the weight of the kiwi fruit and the average rate mentioned in the premise
if fruit_weight_hypothesis <= fruit_weight_premise:
    # check if the hypothesis value contradicts the weight of the fruit in the premise
    label = "contradiction"
elif avg_rate_hypothesis!= avg_rate_premise:
    # check if the average rate in the hypothesis contradicts the average rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
