# Rahul and Deepak's ratio in the premise
ratio_premise = 4/3
# Rahul's age in the premise
rahul_age_premise = 34

# Rahul and Deepak's ratio in the hypothesis
ratio_hypothesis = 6/3
# Rahul's age in the hypothesis
rahul_age_hypothesis = 34

# the hypothesis talks about Rahul's age and the ratio between him and Deepak
# which can be inferred from the premise
if ratio_hypothesis <= ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio in the premise, we can infer the age of Rahul and Deepak
    # from the premise
    label = "entailment"

print(label)
