madan_age_premise = 5
gokul_age_difference_premise = 8
madan_age_hypothesis = 5
gokul_age_difference_hypothesis = 2

# the hypothesis refers to the ages of Gokul and Madan mentioned in the premise
if madan_age_premise != madan_age_hypothesis:
    # check if the age of Madan in the hypothesis contradicts the age of Madan in the premise
    label = "contradiction"
elif gokul_age_difference_hypothesis >= gokul_age_difference_premise:
    # check if the age difference between Gokul and Madan in the hypothesis contradicts the age difference in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
