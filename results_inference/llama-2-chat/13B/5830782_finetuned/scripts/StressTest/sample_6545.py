father_age_premise = 38
father_age_hypothesis = 18
mother_age_premise = 36
mother_age_hypothesis = 36

# the hypothesis talks about the ages of Ayesha's parents when she and her brother were born
if father_age_premise!= father_age_hypothesis:
    # check if the age of the father in the hypothesis contradicts the age of the father in the premise
    label = "contradiction"
elif mother_age_premise!= mother_age_hypothesis:
    # check if the age of the mother in the hypothesis contradicts the age of the mother in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
