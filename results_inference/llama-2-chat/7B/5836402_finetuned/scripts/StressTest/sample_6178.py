ratio_premise = 6/3
ratio_hypothesis = 4/3
future_rahul_age_premise = 34
future_rahul_age_hypothesis = 34

# the hypothesis refers to the ratio and age of Rahul mentioned in the premise
if ratio_hypothesis!= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif future_rahul_age_hypothesis!= future_rahul_age_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age of Rahul in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
