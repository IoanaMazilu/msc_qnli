rahul_age_premise = 34
rahul_age_hypothesis = 34
ratio_premise = 4/3
ratio_hypothesis = 6/3

# the hypothesis refers to the ratio between Rahul and Deepak
if ratio_hypothesis < ratio_premise:
    # check if the hypothesis value contradicts the premise ratio
    label = "contradiction"
elif rahul_age_hypothesis!= rahul_age_premise:
    # check if the estimate of Rahul's age in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
