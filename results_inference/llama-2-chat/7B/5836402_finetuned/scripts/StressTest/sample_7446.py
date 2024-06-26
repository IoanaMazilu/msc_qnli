ratio_rahul_deepak_premise = 4/3
ratio_rahul_deepak_hypothesis = 1/3
future_rahul_age_premise = 26
future_rahul_age_hypothesis = 26

# the hypothesis refers to the ratio and future age of Rahul mentioned in the premise
if ratio_rahul_deepak_hypothesis <= ratio_rahul_deepak_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
elif future_rahul_age_hypothesis!= future_rahul_age_premise:
    # check if the future age of Rahul in the hypothesis contradicts the future age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
