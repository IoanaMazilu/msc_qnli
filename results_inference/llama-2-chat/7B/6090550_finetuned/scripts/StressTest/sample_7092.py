rahul_deepak_ratio_premise = 5/2
rahul_deepak_ratio_hypothesis = 8/2
rahul_age_premise = 26
rahul_age_hypothesis = 26

# the hypothesis refers to the ratio of Rahul and Deepak and Rahul's age mentioned in the premise
if rahul_deepak_ratio_hypothesis <= rahul_deepak_ratio_premise and rahul_age_hypothesis == rahul_age_premise:
    # check if the hypothesis values contradict the premise ones
    label = "entailment"
elif rahul_deepak_ratio_hypothesis > rahul_deepak_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
