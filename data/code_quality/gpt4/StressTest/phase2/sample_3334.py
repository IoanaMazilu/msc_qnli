ratio_premise = 6/3
ratio_hypothesis = 4/3
rahul_age_premise = 26
rahul_age_hypothesis = 26

# the hypothesis mentions the ratio between Rahul and Deepak and Rahul's age after 22 years, which are also mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the proposed 'ratio_hypothesis' contradicts the estimate of less than 'ratio_premise'
    label = "contradiction"
elif rahul_age_hypothesis != rahul_age_premise:
    # check if Rahul's future age in the hypothesis contradicts the one mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
