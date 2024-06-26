age_difference_premise = 7
age_difference_hypothesis = 7

# the hypothesis refers to the age difference between Kiran and Bineesh mentioned in the premise
if age_difference_hypothesis >= age_difference_premise:
    # check if the hypothesis value contradicts the age difference in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
