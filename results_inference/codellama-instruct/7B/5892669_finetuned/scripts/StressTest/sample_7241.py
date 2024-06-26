ayisha_age_ratio_premise = 1/6
ayisha_age_ratio_hypothesis = 1/6

# the hypothesis refers to Ayisha's age in relation to her father's age, mentioned in the premise
if ayisha_age_ratio_hypothesis >= ayisha_age_ratio_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
