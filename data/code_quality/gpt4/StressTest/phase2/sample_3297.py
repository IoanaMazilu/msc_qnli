father_age_premise = 48
mother_age_premise = 46
father_age_hypothesis = 58
mother_age_hypothesis = 46

# the hypothesis refers to the age of Albert's father and mother at the time of her and her brother's birth
if father_age_premise >= father_age_hypothesis:
    # check if the estimated age of Albert's father in the hypothesis contradicts the age provided in the premise
    label = "contradiction"
elif mother_age_premise != mother_age_hypothesis:
    # check if the age of Albert's mother in the hypothesis contradicts the age provided in the premise
    label = "contradiction"
else:
    # if the estimated age of Albert's father and the age of Albert's mother in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
