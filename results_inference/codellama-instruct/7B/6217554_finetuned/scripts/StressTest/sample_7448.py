ratio_rahul_deepak_premise = 4/3
ratio_rahul_deepak_hypothesis = 2/3
rahul_age_premise = 26
rahul_age_hypothesis = 26

# the hypothesis talks about the ratio between Rahul and Deepak and Rahul's age, referenced also in the premise
if ratio_rahul_deepak_hypothesis!= ratio_rahul_deepak_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_hypothesis!= rahul_age_premise:
    # check if Rahul's age in the hypothesis contradicts Rahul's age in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
