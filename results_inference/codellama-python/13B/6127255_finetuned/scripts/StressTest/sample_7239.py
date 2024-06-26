# Ayisha's age divided by her father's age
ayisha_age_factor = 1/6

# Ayisha's age less than 3/6 th of her father's age
ayisha_age_factor_hypothesis = 3/6

# the hypothesis refers to the age ratio between Ayisha and her father mentioned in the premise
if ayisha_age_factor >= ayisha_age_factor_hypothesis:
    # check if the 'ayisha_age_factor' contradicts the age ratio in the hypothesis
    label = "contradiction"
else:
    # if the age ratio in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
