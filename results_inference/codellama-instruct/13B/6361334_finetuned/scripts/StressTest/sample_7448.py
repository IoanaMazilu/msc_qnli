ratio_premise = 4/3
ratio_hypothesis = 2/3
age_premise = 26
age_hypothesis = 26

# the hypothesis refers to the ratio between Rahul and Deepak, which is also mentioned in the premise
if ratio_hypothesis!= ratio_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif age_hypothesis!= age_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
