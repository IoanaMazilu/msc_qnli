kiran_age_premise = 9
bineesh_age_premise = 7

# the hypothesis refers to the age difference between Kiran and Bineesh
if kiran_age_premise - bineesh_age_premise < 7:
    # check if the hypothesis value contradicts the age difference in the premise
    label = "contradiction"
else:
    # the premise gives an exact age difference and a ratio between the ages
    # any age difference less than 7 years and a ratio of 7:9 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
