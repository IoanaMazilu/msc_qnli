total_age_premise = 66
total_age_hypothesis = 66

# the hypothesis refers to the total age of Amar, Akbar and Anthony mentioned in the premise
if total_age_hypothesis >= total_age_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
