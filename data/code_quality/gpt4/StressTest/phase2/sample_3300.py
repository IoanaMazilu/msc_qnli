ratio_premise = 4 / 3
ratio_hypothesis = 8 / 3
rahul_age_premise = 38
rahul_age_hypothesis = 38

# the hypothesis refers to both the ratio between Rahul and Deepak, and Rahul's future age, which are also mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the hypothesis value contradicts the estimate of 'ratio_premise'
    label = "contradiction"
elif rahul_age_hypothesis != rahul_age_premise:
    # check if Rahul's future age in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
