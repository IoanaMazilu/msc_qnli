total_age_premise = 66
total_age_hypothesis = 66

# the hypothesis refers to the total age of Amar, Akbar and Anthony mentioned in the premise
if total_age_hypothesis >= total_age_premise:
    # check if the estimate of 'total_age_hypothesis' contradicts the total age in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
