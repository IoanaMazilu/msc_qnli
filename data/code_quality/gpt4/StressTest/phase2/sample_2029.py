old_ratio_premise = 6/3
old_ratio_hypothesis = 5/3

# the hypothesis states a possible value for the age ratio in the future, also mentioned in the premise
if old_ratio_hypothesis > old_ratio_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'old_ratio_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise estimate, we infer entailment
    label = "entailment"

print(label)
