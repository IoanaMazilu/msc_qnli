jane_age_start_premise = 20
jane_age_start_hypothesis = 40

# the hypothesis refers to Jane's age when she started baby-sitting, which is also mentioned in the premise
if jane_age_start_hypothesis >= jane_age_start_premise:
    # check if the hypothesis value contradicts the premise value of 'jane_age_start_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than 'jane_age_start_premise', it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
