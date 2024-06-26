father_age_premise = 48
father_age_hypothesis = 38
mother_age_premise = 36
mother_age_hypothesis = 36

# the hypothesis refers to the age of Ayesha's parents when she and her brother were born
if father_age_hypothesis >= father_age_premise:
    # check if the age of Ayesha's father at her birth in the hypothesis contradicts the premise (her father being less than 48 years old when she was born)
    label = "contradiction"
elif mother_age_hypothesis != mother_age_premise:
    # check if the age of Ayesha's mother at her brother's birth in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
