father_age_premise = 60
father_age_hypothesis = 40
mother_age_premise = 32
mother_age_hypothesis = 32

# the hypothesis refers to the age of Ayesha's parents when she and her brother were born, which is also mentioned in the premise
if father_age_hypothesis >= father_age_premise:
    # check if the hypothesis value contradicts the estimate of 'father_age_premise'
    label = "contradiction"
elif mother_age_hypothesis != mother_age_premise:
    # check if the age of Ayesha's mother at the time her brother was born contradicts the age mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the age of Ayesha's father
    # any age less than 'father_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
