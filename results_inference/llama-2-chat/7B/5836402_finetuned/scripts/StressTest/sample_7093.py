ratio_premise = 8/2
ratio_hypothesis = 5/2
future_rahul_age_premise = 26
future_rahul_age_hypothesis = 26

# the hypothesis refers to the ratio and the age of Rahul mentioned in the premise
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
