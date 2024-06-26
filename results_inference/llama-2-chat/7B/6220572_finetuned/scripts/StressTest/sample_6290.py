kiwi_fruit_weight_premise = 8
kiwi_fruit_weight_hypothesis = 8
rate_premise = 360
rate_hypothesis = 360

# the hypothesis talks about the weight and rate of kiwi fruit, referenced also in the premise
if kiwi_fruit_weight_hypothesis!= kiwi_fruit_weight_premise:
    # check if the number of kiwi fruit weight in the hypothesis contradicts the number of kiwi fruit weight reported in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate of kiwi fruit in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
