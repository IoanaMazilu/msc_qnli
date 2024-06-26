age_ratio_premise = 5/3
age_ratio_hypothesis = 7/3

# the hypothesis refers to the age ratio mentioned in the premise
if age_ratio_premise >= age_ratio_hypothesis:
    # check if the 'age_ratio_premise' contradicts the age ratio in the hypothesis
    label = "contradiction"
else:
    # if the age ratio in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
