neelam_age_ratio_premise = 5
neelam_age_ratio_hypothesis = 4
shaan_age_ratio_premise = 9
shaan_age_ratio_hypothesis = 9

# the hypothesis refers to the ratio between the one-third age of Neelam and half of Shaan's age mentioned in the premise
if neelam_age_ratio_hypothesis >= neelam_age_ratio_premise:
    # check if the estimate of 'neelam_age_ratio_hypothesis' contradicts the number of 'neelam_age_ratio_premise' in the premise
    label = "contradiction"
elif shaan_age_ratio_premise != shaan_age_ratio_hypothesis:
    # check if the number of 'shaan_age_ratio_hypothesis' in the hypothesis contradicts the number of 'shaan_age_ratio_premise' reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
