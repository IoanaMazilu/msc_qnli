ayisha_age_premise = 3/6
ayisha_age_hypothesis = 1/6

# the hypothesis refers to Ayisha's age, which is also mentioned in the premise
if ayisha_age_hypothesis!= ayisha_age_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
