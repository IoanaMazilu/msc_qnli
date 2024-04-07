# Premise: Rajesh is less than 70 years old and Mary is 30 years old.
# Hypothesis: Rajesh is 20 years old and Mary is 30 years old.
# Golden Label: neutral

rajesh_age_premise = 70
rajesh_age_hypothesis = 20
mary_age_premise = 30
mary_age_hypothesis = 30

# the hypothesis talks about the ages of Rajesh and Mary, referenced also in the premise
if rajesh_age_hypothesis >= rajesh_age_premise:
    # check if the hypothesis value contradicts the estimate of less than 'rajesh_age_premise'
    label = "contradiction"
elif mary_age_hypothesis != mary_age_premise:
    # check if the age of Mary in the hypothesis contradicts the age of Mary reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of Rajesh
    # any age less than 'rajesh_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

