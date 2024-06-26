ratio_premise = 8/2
ratio_hypothesis = 5/2
age_premise = 26

# check if the ratio in the hypothesis contradicts the ratio in the premise
if ratio_hypothesis!= ratio_premise:
    label = "contradiction"
elif age_premise!= age_hypothesis:
    # check if the age of Rahul in the hypothesis contradicts the age of Rahul in the premise
    label = "contradiction"
else:
    # if the ratio and age values in the hypothesis are consistent with the premise, we can infer neutrality
    label = "neutral"

print(label)
