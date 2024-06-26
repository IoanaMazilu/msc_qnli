yhat = 7/3

# the hypothesis refers to the same scenario as the premise
# compute the ratio of ages in the premise and hypothesis
ratio_age_premise = 5/3
ratio_age_hypothesis = 7/3

if ratio_age_hypothesis <= ratio_age_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
