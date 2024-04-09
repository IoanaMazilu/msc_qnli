ratio_premise = 6/3
ratio_hypothesis = 4/3
age_premise = 34

# the hypothesis refers to the ratio of Rahul and Deepak and the age of Rahul after 6 years
if ratio_hypothesis <= ratio_premise:
    # check if the estimate of 'ratio_hypothesis' contradicts the ratio reported in the premise
    label = "contradiction"
elif age_premise!= age_hypothesis:
    # check if the age of Rahul in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
