father_age_premise = 1/6
father_age_hypothesis = 3/6
ayisha_age_premise = father_age_premise
ayisha_age_hypothesis = father_age_hypothesis

# the hypothesis refers to Ayisha's age in relation to her father's age
if ayisha_age_hypothesis < ayisha_age_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif ayisha_age_hypothesis > father_age_premise:
    # the hypothesis entails the premise
    label = "entailment"
else:
    # the premise only gives an estimate for Ayisha's age
    # any age less than 3/6 of her father's age is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
