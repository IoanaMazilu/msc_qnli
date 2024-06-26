ayisha_age_fraction_premise = 1/6
ayisha_age_fraction_hypothesis = 1/6

# the hypothesis refers to the fraction of Ayisha's age compared to her father's age mentioned in the premise
if ayisha_age_fraction_hypothesis >= ayisha_age_fraction_premise:
    # check if the hypothesis value contradicts the fraction of Ayisha's age in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
