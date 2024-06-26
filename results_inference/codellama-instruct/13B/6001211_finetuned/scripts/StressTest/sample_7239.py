ayisha_age_premise = 1/6
ayisha_age_hypothesis = 3/6

# the hypothesis refers to Ayisha's age in relation to her father's age, as stated in the premise
if ayisha_age_hypothesis <= ayisha_age_premise:
    # check if the hypothesis value contradicts the premise value of 'ayisha_age_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
