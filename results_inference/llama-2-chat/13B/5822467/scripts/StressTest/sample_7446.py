rahul_age_premise = 26
rahul_age_hypothesis = 26
ratio_premise = 4/3
ratio_hypothesis = 1/3

# the hypothesis refers to the ratio between Rahul and Deepak, and the age of Rahul after 6 years
if ratio_hypothesis > ratio_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif rahul_age_hypothesis!= rahul_age_premise:
    # the hypothesis does not contradict the premise, but the estimate of Rahul's age after 6 years does
    label = "neutral"
else:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
