ratio_premise = 4/3
ratio_hypothesis = 1/3
rahul_age_premise = 26
rahul_age_hypothesis = 26

# the hypothesis refers to the ratio of Rahul and Deepak and Rahul's age mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
elif rahul_age_hypothesis!= rahul_age_premise:
    # check if the age of Rahul in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
