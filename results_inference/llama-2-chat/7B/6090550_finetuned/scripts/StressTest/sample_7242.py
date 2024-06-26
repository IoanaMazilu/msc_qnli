father_age_premise = 2 * shankar_age_premise + 10
father_age_hypothesis = 2 * shankar_age_hypothesis + 80

# the hypothesis refers to the future age of Ayisha's father, which is also mentioned in the premise
# however, the hypothesis provides a different time frame for this future age
if father_age_hypothesis <= father_age_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
