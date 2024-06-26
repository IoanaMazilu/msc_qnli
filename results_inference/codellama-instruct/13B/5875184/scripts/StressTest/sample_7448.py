ratio_premise = 4/3
ratio_hypothesis = 2/3
age_premise = 26
age_hypothesis = 26

# the hypothesis refers to the ratio between Rahul and Deepak, which is mentioned in the premise
if ratio_premise!= ratio_hypothesis:
    # check if the hypothesis value contradicts the ratio mentioned in the premise
    label = "contradiction"
elif age_premise!= age_hypothesis:
    # check if the age mentioned in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
