ratio_age_premise = 5/3
ratio_age_hypothesis = 7/3

# the hypothesis refers to the ratio of their ages in the future, which is also mentioned in the premise
if ratio_age_hypothesis <= ratio_age_premise:
    # check if the hypothesis value contradicts the estimate of 'ratio_age_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
