age_ratio_premise = 7/9
age_ratio_hypothesis = 5/9

# the hypothesis talks about the age ratio of two people, that is also mentioned in the premise
if age_ratio_hypothesis != age_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio mentioned in the premise
    label = "contradiction"
else:
    # if the age ratios match, we can infer entailment
    label = "entailment"

print(label)
