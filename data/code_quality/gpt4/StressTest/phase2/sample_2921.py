# define the ration between Rahul and Deepak in the premise and hypothesis
ratio_premise = 4/2
ratio_hypothesis = 5/2

# define the age of Rahul in 6 years in the premise and hypothesis
raul_age_premise = 22
raul_age_hypothesis = 22

# the hypothesis refers to the ratio between Rahul and Deepak and Rahul's age in 6 years, both mentioned in the premise
if ratio_premise != ratio_hypothesis:
    # check if the ratio between Rahul and Deepak in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif raul_age_premise != raul_age_hypothesis:
    # check if Rahul's age in 6 years in the hypothesis contradicts Rahul's age in 6 years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
